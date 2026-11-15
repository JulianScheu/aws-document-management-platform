"""DocuWorks prototype: document workflow + SQLite metadata + local/S3 file storage.

For local development only: HTTP on 127.0.0.1, without employee authentication.
For AWS deployment, keep access private until a secure access design is implemented.
"""

from datetime import datetime, timezone
from io import BytesIO
from pathlib import Path
import os
import sqlite3
from uuid import uuid4

from flask import Flask, abort, flash, redirect, render_template_string, request, send_file, url_for
from werkzeug.exceptions import RequestEntityTooLarge
from werkzeug.utils import secure_filename


STATUSES = ("RECEIVED", "IN_REVIEW", "PROCESSED")
PAGE = """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>DocuWorks | Document Register</title>
<style>
body{font-family:system-ui,-apple-system,sans-serif;max-width:950px;margin:45px auto;padding:0 20px;color:#20252c;background:#fafafa}
h1{margin-bottom:4px}p.sub{color:#596271;margin-top:0}
section{background:white;border:1px solid #dedfe3;border-radius:8px;padding:20px;margin:20px 0}
form{display:flex;flex-wrap:wrap;gap:10px;align-items:center}
input,select,button{font:inherit;padding:8px;border:1px solid #bbc0c9;border-radius:5px}
button{background:#233650;color:white;cursor:pointer}
table{border-collapse:collapse;width:100%}th,td{border-bottom:1px solid #e0e2e7;padding:10px;text-align:left}
small{color:#596271}.notice{padding:10px;background:#edf5ff;border-radius:5px}
@media(max-width:700px){table{font-size:13px}th,td{padding:5px}}
</style></head><body>
<h1>DocuWorks</h1><p class="sub">Technical document register · Training prototype</p>
{% for message in get_flashed_messages() %}<p class="notice">{{ message }}</p>{% endfor %}
<section><h2>Register document</h2>
<form method="post" action="{{ url_for('upload') }}" enctype="multipart/form-data">
<input name="title" placeholder="Document title" required maxlength="120">
<input type="file" name="document" required><button type="submit">Upload</button>
</form><small>Test documents only. Maximum file size: 20 MB.</small></section>
<section><h2>Documents</h2>
<form method="get" action="{{ url_for('index') }}">
<input name="q" value="{{ q }}" placeholder="Search title or file name">
<button type="submit">Search</button></form>
<table><thead><tr><th>Title</th><th>File</th><th>Created (UTC)</th><th>Status</th><th>Download</th></tr></thead><tbody>
{% for d in docs %}
<tr><td>{{ d['title'] }}</td><td>{{ d['filename'] }}</td><td>{{ d['created_at'] }}</td>
<td><form method="post" action="{{ url_for('update_status', document_id=d['id']) }}">
<select name="status" aria-label="Document processing status">
{% for s in statuses %}<option value="{{ s }}" {% if d['status']==s %}selected{% endif %}>{{ s }}</option>{% endfor %}
</select><button type="submit">Save</button></form></td>
<td><a href="{{ url_for('download', document_id=d['id']) }}">Download</a></td></tr>
{% else %}<tr><td colspan="5">No documents found.</td></tr>{% endfor %}
</tbody></table></section><small>Prototype only: no user login or HTTPS; do not expose publicly.</small>
</body></html>"""


def create_app(config=None):
    app = Flask(__name__)
    app.config.update(
        SECRET_KEY=os.getenv("DOCUWORKS_SECRET_KEY", "local-development-only"),
        DATA_DIR=os.getenv("DOCUWORKS_DATA_DIR", "./var"),
        STORAGE_BACKEND=os.getenv("DOCUWORKS_STORAGE", "local"),
        S3_BUCKET=os.getenv("DOCUWORKS_S3_BUCKET", ""),
        MAX_CONTENT_LENGTH=20 * 1024 * 1024,
    )
    if config:
        app.config.update(config)
    data_dir = Path(app.config["DATA_DIR"]).expanduser().resolve()
    data_dir.mkdir(parents=True, exist_ok=True)
    local_files = data_dir / "documents"
    if app.config["STORAGE_BACKEND"] == "local":
        local_files.mkdir(exist_ok=True)
    elif app.config["STORAGE_BACKEND"] == "s3":
        if not app.config["S3_BUCKET"]:
            raise ValueError("DOCUWORKS_S3_BUCKET is required for S3 storage")
    else:
        raise ValueError("DOCUWORKS_STORAGE must be 'local' or 's3'")
    db_path = data_dir / "docuworks.db"

    def db():
        con = sqlite3.connect(db_path)
        con.row_factory = sqlite3.Row
        return con

    with db() as con:
        con.execute("""CREATE TABLE IF NOT EXISTS documents (
            id TEXT PRIMARY KEY, title TEXT NOT NULL, filename TEXT NOT NULL,
            status TEXT NOT NULL, created_at TEXT NOT NULL
        )""")
        con.execute("CREATE INDEX IF NOT EXISTS idx_documents_title ON documents(title)")

    def storage_put(key, data):
        if app.config["STORAGE_BACKEND"] == "local":
            (local_files / key).write_bytes(data)
        else:
            import boto3
            boto3.client("s3").put_object(
                Bucket=app.config["S3_BUCKET"], Key=f"documents/{key}",
                Body=data, ContentType="application/octet-stream")

    def storage_get(key):
        if app.config["STORAGE_BACKEND"] == "local":
            p = local_files / key
            if not p.is_file():
                abort(404, "File not found")
            return p.read_bytes()
        import boto3
        from botocore.exceptions import ClientError
        try:
            response = boto3.client("s3").get_object(
                Bucket=app.config["S3_BUCKET"], Key=f"documents/{key}")
        except ClientError as ex:
            if ex.response.get("Error", {}).get("Code") in ("NoSuchKey", "404"):
                abort(404, "File not found")
            raise
        return response["Body"].read()

    @app.get("/")
    def index():
        q = request.args.get("q", "").strip()[:120]
        with db() as con:
            if q:
                docs = con.execute(
                    "SELECT * FROM documents WHERE title LIKE ? OR filename LIKE ? ORDER BY created_at DESC",
                    (f"%{q}%", f"%{q}%")).fetchall()
            else:
                docs = con.execute("SELECT * FROM documents ORDER BY created_at DESC").fetchall()
        return render_template_string(PAGE, docs=docs, q=q, statuses=STATUSES)

    @app.post("/upload")
    def upload():
        title = request.form.get("title", "").strip()[:120]
        uploaded = request.files.get("document")
        if not title or uploaded is None or not uploaded.filename:
            abort(400, "Title and document are required")
        filename = secure_filename(uploaded.filename)
        if not filename:
            abort(400, "Invalid file name")
        document_id = uuid4().hex
        payload = uploaded.read()
        storage_put(document_id, payload)
        with db() as con:
            con.execute("INSERT INTO documents VALUES (?, ?, ?, ?, ?)",
                        (document_id, title, filename, "RECEIVED",
                         datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")))
        app.logger.info("Uploaded document id=%s", document_id)
        flash("Document uploaded and registered.")
        return redirect(url_for("index"))

    @app.get("/download/<document_id>")
    def download(document_id):
        with db() as con:
            entry = con.execute("SELECT * FROM documents WHERE id=?", (document_id,)).fetchone()
        if not entry:
            abort(404)
        content = storage_get(document_id)
        return send_file(BytesIO(content), mimetype="application/octet-stream",
                         as_attachment=True, download_name=entry["filename"])

    @app.post("/status/<document_id>")
    def update_status(document_id):
        status = request.form.get("status", "")
        if status not in STATUSES:
            abort(400, "Unknown status")
        with db() as con:
            cursor = con.execute("UPDATE documents SET status=? WHERE id=?", (status, document_id))
            if cursor.rowcount == 0:
                abort(404)
        app.logger.info("Updated document id=%s status=%s", document_id, status)
        flash("Processing status updated.")
        return redirect(url_for("index"))

    @app.errorhandler(RequestEntityTooLarge)
    def too_large(_error):
        return "File exceeds the 20 MB demo limit", 413

    return app


if __name__ == "__main__":
    create_app().run(host="127.0.0.1", port=5000, debug=False)
