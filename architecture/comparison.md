# Architecture comparison and proposed selection

| Criterion | Option A: EC2/EBS/S3 | Option B: API Gateway/Lambda/DynamoDB/S3 |
| --- | --- | --- |
| Requirement fit | **High** for existing Linux app | Medium; assumes app redesign |
| Ease of migration | Lower refactoring effort | Significant application rewrite likely |
| Availability | Single-instance outage risk | Managed services; application design still matters |
| Storage persistence | EBS volume + S3 objects | DynamoDB metadata + S3 objects |
| Backup/recovery | EBS snapshot, S3 strategy | Managed data backup/versioning strategy |
| Security | Instance, IAM, SG, storage protection | API authorization, Lambda IAM, storage protection |
| Scaling | Requires capacity changes/further architecture | Managed per-request scaling subject to quotas |
| Cost | Instance, EBS, public IPv4 even when idle | Per request/usage; costs depend on configuration |
| Operations | Higher OS and runtime effort | Less server maintenance, more app/API work |
| Time/scope risk | **Manageable** with sample app | Higher due to code rewrite |

## Provisional decision: Option A
The stated task is migration of an existing internal application, not the redesign of its complete business logic. Option A allows the smallest useful demonstration of compute, network access, independent storage, infrastructure reproducibility, backup and recovery. The design must remain secure and cost-conscious.

## Explicit limitations
- One-instance design cannot guarantee continuous availability.
- EBS data durability does not equal successful recovery; recovery must be tested.
- The first code version does not provide an authenticated HTTPS endpoint for 10–20 employees. Treat this as a deployment limitation and future improvement; do not claim that production employee access is already implemented.

## Decision status
Draft for student/instructor review; finalized only after cost/security review and practical AWS validation.
