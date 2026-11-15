# DocuWorks verification record — updated 2026-11-15

Evidence below describes tests actually performed, not merely planned. All application documents are synthetic.

| ID | Scenario | Status / evidence |
| --- | --- | --- |
| T-01 | `terraform fmt`, `init`, `validate` | **PASS** — provider installed, validation successful |
| T-02 | `terraform apply` | **PASS** — 18 added, 0 changed, 0 destroyed |
| T-03 | EC2 and admin network connection | **PASS** — SSM Session Manager connected |
| T-04 | Reject unauthorized inbound access | **PARTIAL** — security group configured without ingress; negative access test pending |
| T-05 | Application via restricted browser tunnel | **PASS** — SSM forwarding Mac port 8765 to EC2 localhost:5000, HTTP 200 |
| T-06 | Upload object to private S3 | **PASS** — upload via Flask and S3 HEAD check |
| T-07 | Document retrieval and status updates | **PASS** — S3 GET and browser download contents checked; status changed |
| T-08 | EC2 restart and EBS persistence | **PASS** — `/data` auto-mounted; SQLite records and S3 objects remained available |
| T-09 | Replace EC2 and attach/restore data | **NOT TESTED** |
| T-10 | Create EBS snapshot | **PASS** — `snap-0af6e7490c0fcb177`, status `completed` |
| T-11 | Restore SQLite data from snapshot | **NOT TESTED** — snapshot existence does not prove recovery |
| T-12 | CloudWatch logs / metrics | **NOT TESTED** — `journalctl` verifies local service log only |
| T-13 | Terraform destroy and cost cleanup | **NOT DONE** — infrastructure retained for continuing the project |
| T-14 | Automated Python tests | **PASS** — 3 unittest scenarios passed locally |
| T-15 | Linux service availability | **PASS** — systemd active and Gunicorn returns HTTP 200 |

## Captured visual evidence
- [Browser application](../evidence/2026-11-15/01-docuworks-application.png): two synthetic documents and processing statuses
- [EC2](../evidence/2026-11-15/02-ec2-instance.png): provisioned instance, deliberately stopped after testing
- [S3](../evidence/2026-11-15/03-s3-documents.png): two document objects
- [EBS snapshot](../evidence/2026-11-15/04-ebs-snapshot.png): backup marked completed

## Remaining evidence to capture
- Terraform apply and EBS mount terminal evidence, if needed for final review
- Recovery test using a separate restored EBS volume
- CloudWatch monitoring and logs
- Security negative test
- Confirm service starts after a second EC2 reboot (systemd auto-start)
- Terraform and application provisioning reproducibility
