# Verification plan (NOT YET RUN)

| Test ID | Scenario | Evidence | Status |
| --- | --- | --- | --- |
| T-01 | `terraform fmt`, `init`, `validate` | CLI output | Not run |
| T-02 | `terraform apply` | Resources and plan output | Not run |
| T-03 | Network connectivity and admin access | SSM managed node/session | Not run |
| T-04 | Block unauthorized inbound access | SG and connection result | Not run |
| T-05 | Application reachable by authorized test user | Demo / HTTP result | Not run |
| T-06 | Upload file to private S3 | Object present + app result | Not run |
| T-07 | Retrieve uploaded document | File contents verified | Not run |
| T-08 | Restart Linux instance and read app data | Persistence evidence | Not run |
| T-09 | Replace/recreate app instance, reattach/restore data | Persistence evidence | Not run |
| T-10 | Create EBS snapshot | Snapshot ID/time | Not run |
| T-11 | Restore data from snapshot | Restored files checksum | Not run |
| T-12 | CloudWatch logs / metrics | Screenshot and metric description | Not run |
| T-13 | Terraform destroy and manual cost check | Resource inventory | Not run |

Use synthetic test documents. Do not fabricate execution evidence.
