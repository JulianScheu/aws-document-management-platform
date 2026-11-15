"""Run with: python -m unittest discover -s tests -p 'test_*.py' -v"""

from io import BytesIO
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "application"))
from app import create_app


class DocumentWorkflowTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.config = {"TESTING": True, "DATA_DIR": self.temp.name,
                       "STORAGE_BACKEND": "local", "SECRET_KEY": "test-secret"}
        self.app = create_app(self.config)
        self.client = self.app.test_client()

    def tearDown(self):
        self.temp.cleanup()

    def test_document_upload_download_search_and_status(self):
        result = self.client.post("/upload", data={
            "title": "Maintenance report – Pump P-101",
            "document": (BytesIO(b"Pump tested successfully"), "report.txt")
        }, content_type="multipart/form-data", follow_redirects=True)
        self.assertEqual(result.status_code, 200)
        self.assertIn(b"Maintenance report", result.data)

        with self.app.app_context():
            import sqlite3
            con = sqlite3.connect(Path(self.temp.name) / "docuworks.db")
            try:
                doc_id = con.execute("SELECT id FROM documents").fetchone()[0]
            finally:
                con.close()

        response = self.client.get(f"/download/{doc_id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b"Pump tested successfully")
        response = self.client.get("/?q=Pump")
        self.assertIn(b"Maintenance report", response.data)
        response = self.client.post(f"/status/{doc_id}",
                                    data={"status": "PROCESSED"}, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"PROCESSED", response.data)

        # Simulate application process restart with the same persistent data directory.
        restarted = create_app(self.config).test_client()
        self.assertEqual(restarted.get(f"/download/{doc_id}").data,
                         b"Pump tested successfully")

    def test_rejects_invalid_status(self):
        response = self.client.post("/status/unknown", data={"status": "DELETED"})
        self.assertEqual(response.status_code, 400)

    def test_rejects_missing_upload(self):
        self.assertEqual(self.client.post("/upload", data={"title": "Only a title"}).status_code, 400)


if __name__ == "__main__":
    unittest.main()
