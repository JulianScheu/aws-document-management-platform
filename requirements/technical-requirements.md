# Technical and non-functional requirements

## Functional technical requirements
- **TR-01:** Linux-based application runtime hosted in AWS.
- **TR-02:** AWS network with controlled access and explicitly documented traffic path.
- **TR-03:** Persistent application data; storage must not depend on the EC2 root disk surviving replacement.
- **TR-04:** Document upload/download using a suitable object-storage mechanism.
- **TR-05:** Backup process with defined source, frequency, retention, destination and restoration steps.
- **TR-06:** IAM permissions following least privilege; no embedded AWS access keys.
- **TR-07:** Basic CloudWatch logs, metrics and operational checks.
- **TR-08:** Terraform-managed infrastructure; no console-only final environment.
- **TR-09:** At least one actual recovery demonstration and validation of restored data.

## Non-functional requirements
| Area | Goal | Trade-off |
| --- | --- | --- |
| Security | Restrict administrative and document access | More access configuration required |
| Data durability | Documents and critical app data survive compute failure | Independent storage and backups |
| Availability | Suitable for a small internal service | Single instance can have downtime; document limitation |
| Reliability | Recoverability is tested | Requires actual restore exercise |
| Scalability | Allow gradual growth | Avoid premature multi-region complexity |
| Cost | Minimize unnecessary continuously running services | Simple initial topology |
| Maintainability | Infrastructure is readable, repeatable and documented | Clear naming and Terraform structure |

## Out of scope for initial version
- Thousands of simultaneous users
- Multi-region active/active
- Kubernetes
- Large custom web application
- Claims of zero downtime
