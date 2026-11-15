# AWS service analysis

| Capability | Candidate services | Initial decision / rationale |
| --- | --- | --- |
| Compute | EC2, ECS Fargate, Lambda | **EC2** offers a straightforward Linux runtime for a small existing application |
| Application data | EBS, EFS, RDS | **EBS** independent data volume for a single-instance prototype; cannot attach across AZs |
| Uploaded documents | S3, EBS, EFS | **S3** private bucket separates document objects from instance lifecycle |
| Networking | VPC, subnet, routes, IGW, SG | Small VPC/subnet/SG; no inbound access initially |
| AWS permissions | IAM roles/policies | Instance profile avoids long-lived AWS keys |
| Admin access | Systems Manager Session Manager | No open SSH port required; needs instance managed and SSM connectivity |
| Monitoring | CloudWatch | Logs, system metrics, alarms as needed |
| Backups | EBS snapshots, S3 versioning | Test a snapshot restore; versioning helps with object changes but is not by itself an independent backup |
| Budget control | AWS Budgets | Set billing notifications manually/account-wide as appropriate |

**Deliberately not included at first:** NAT Gateway, ALB, EKS, multi-AZ RDS. They add cost and operational complexity without a demonstrated requirement at this scale.
