# DocuWorks project checklist

**Last updated:** 2026-11-15. Checkmarks represent verified work, not just planned work.

## Requirements and design
- [x] Create GitHub repository with business/technical requirements and architecture drafts.
- [x] Document two architecture alternatives and a comparison.
- [x] Draft four Architecture Decision Records (ADRs).
- [ ] Review the requirements, assumptions, diagrams and ADR trade-offs with the instructor.
- [ ] Complete final AWS architecture diagram with AWS service icons.

## AWS foundation
- [x] Select and verify AWS account/Region `eu-central-1`; create a monthly AWS budget.
- [ ] Verify budget notification thresholds and assess actual monthly cost drivers.
- [x] Run `terraform fmt`, `init`, `validate` and review `plan`.
- [x] Deploy infrastructure with Terraform: 18 added, 0 changed, 0 destroyed.
- [x] Verify EC2 access through SSM without opening inbound SSH/HTTP.
- [x] Mount the dedicated encrypted 8 GB XFS EBS volume under `/data` using its UUID.
- [x] Verify S3 private document storage through the EC2 IAM role.
- [ ] Automate Linux installation, volume setup and application deployment.

## Application and testing
- [x] Deploy Flask on EC2 with Python 3.12, Gunicorn and systemd.
- [x] Verify browser access over SSM port forwarding.
- [x] Verify upload, S3 storage, download and processing-status changes with synthetic industrial reports.
- [x] Pass three local Python application tests.
- [x] Verify EBS remount, SQLite records and S3 document retrieval after an EC2 reboot.
- [x] Capture four real screenshots in `evidence/2026-11-15/`.
- [ ] Demonstrate automatic Gunicorn/systemd start after a new EC2 reboot.

## Backup, monitoring and security
- [x] Create a completed EBS data snapshot `snap-0af6e7490c0fcb177`.
- [ ] Restore the snapshot to a separate EBS volume and verify recovered SQLite data.
- [ ] Define and implement a repeatable backup schedule, retention and recovery procedure.
- [ ] Implement CloudWatch monitoring and centralized logs; test an operational alert if practical.
- [ ] Perform a negative security-access test and document the result.
- [ ] Evaluate a suitable authenticated/HTTPS employee access approach.

## Final review and cleanup
- [ ] Update tests and evidence after recovery/monitoring implementation.
- [ ] Complete AWS Well-Architected, security and cost evaluations.
- [ ] Create final presentation and demonstrate the full solution.
- [ ] Run `terraform destroy` after final demonstration and verify billable resources are cleaned up.

**Current limitation:** Terraform provisions the AWS foundation; the Linux/application setup is still manual. A snapshot exists, but actual recovery has **not** been proven yet.
