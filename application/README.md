# DocuWorks application — first working prototype

A small document register for an industrial document-processing workflow. Staff can upload a test document, search by title/file name, download it and change its processing status (`RECEIVED`, `IN_REVIEW`, `PROCESSED`).

**Currently a development prototype:** no user accounts, authentication, HTTPS, or CSRF protection. It is intentionally bound to `127.0.0.1` and **must not be exposed to the public internet**. Use synthetic data only.

## Run locally on the Mac

From the repository root:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r application/requirements.txt
python application/app.py
```

Then open `http://127.0.0.1:5000` in your browser.

By default, application metadata is stored in `./var/docuworks.db` (SQLite), and document files in `./var/documents/`. These local files are development data and must not be committed to Git. The local backend lets you check the workflow before any AWS resources are deployed.

## Run automated tests

```bash
python -m unittest discover -s tests -p 'test_*.py' -v
```

The tests cover upload, download, search, status change, invalid inputs and persistence across app initialization. This is **not** an EC2 replacement or EBS snapshot recovery test.

## AWS storage configuration (later deployment)

For EC2, store the SQLite database on the mounted EBS data volume and use private S3 for document files:

```bash
export DOCUWORKS_DATA_DIR=/data/docuworks
export DOCUWORKS_STORAGE=s3
export DOCUWORKS_S3_BUCKET=<bucket-name-from-terraform-output>
```

The application uses `boto3`'s standard credential chain. On EC2, it should obtain credentials through the existing IAM instance profile. **Do not add access keys to source files.**

We will add a secure entry point, service startup, EC2/EBS mount configuration, operational logs and a tested restore workflow in subsequent steps.

## Design limitation worth documenting

The S3 object is uploaded before its SQLite metadata is committed. If that database transaction fails, the S3 object may remain without a metadata record. A production implementation should add reconciliation/cleanup, validation, authentication and other appropriate controls.
