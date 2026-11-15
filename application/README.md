# DocuWorks application — working proof of concept

A small document register for a synthetic industrial maintenance/quality-report workflow. The user can upload a test file, search by title/file name, download it and update its current processing status (`RECEIVED`, `IN_REVIEW`, `PROCESSED`). This is not a full approval or audit-trail system.

**Security limitation:** No employee accounts, authentication, HTTPS or CSRF protection. Bind the server to `127.0.0.1`; **do not expose this prototype publicly**. Use only synthetic files.

## Run locally

From the repository root:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r application/requirements.txt
python application/app.py
```

Open `http://127.0.0.1:5000`. By default, SQLite metadata is saved in `./var/docuworks.db` and test document files in `./var/documents/`; both are ignored by Git. The local backend allows tests without AWS infrastructure.

## Run automated tests

```bash
python -m unittest discover -s tests -p 'test_*.py' -v
```

Three local tests passed on 2026-11-15: the document workflow including a simulated app reinitialization, invalid status handling, and invalid upload rejection. This is **not** an EBS snapshot restore test.

## AWS deployment — manually configured on 2026-11-15

The application was deployed to an Amazon Linux 2023 EC2 instance using Python 3.12, Gunicorn 23 and systemd. The AWS foundation was created with Terraform, but installing the app, mounting EBS and creating `docuworks.service` were **manual** steps. A replacement instance cannot yet be rebuilt from Terraform alone.

Runtime configuration on EC2:

```bash
export AWS_DEFAULT_REGION=eu-central-1
export DOCUWORKS_DATA_DIR=/data/docuworks
export DOCUWORKS_STORAGE=s3
export DOCUWORKS_S3_BUCKET=<bucket-name-from-terraform-output>
```

- **SQLite metadata:** `/data/docuworks/docuworks.db`, on a dedicated 8 GB XFS EBS volume mounted at `/data`.
- **Document objects:** `documents/<generated-id>` inside the private S3 bucket.
- **Credentials:** `boto3` uses the EC2 IAM instance profile; no static AWS access keys are stored in the app.
- **Service:** systemd runs Gunicorn bound to `127.0.0.1:5000`.
- **Browser access:** the demonstration used authorized SSM port forwarding from Mac `localhost:8765` to the instance port 5000.

On the EC2 instance, inspect the service using:

```bash
systemctl status docuworks --no-pager
sudo journalctl -u docuworks -n 50 --no-pager
```

The EC2 restart test verified that the data volume mounted automatically and that SQLite/S3 records remained available. A separate EBS snapshot was completed, but **actual recovery has not yet been tested**. CloudWatch logging and automatic Linux/application provisioning are pending.

## Known application limitation

The S3 object is uploaded before its SQLite metadata transaction commits. If the database write fails, an S3 object may exist without a database record. A production implementation needs reconciliation/cleanup, robust input validation, authorization and other controls. S3 versioning alone is not a complete backup strategy.
