# DocuWorks | AWS Document Management Platform

**DCI Final Project — Implementation / Cloud Infrastructure**  
**AWS Region:** `eu-central-1` (proposed)  
**Status:** Week 1/2 documents drafted; AWS infrastructure **not deployed or tested**.

## Business problem
A small company (10–20 employees) operates an internal document-management application on one physical server. Uploaded documents and application data reside together, backups are manual, and server failure interrupts availability. The company needs a cost-conscious, secure AWS migration.

## Project objectives
- Design and compare **two** AWS architecture options.
- Deploy a small Linux application environment using **Terraform**.
- Keep uploaded documents separately from the application environment.
- Demonstrate persistent application data and backup/recovery.
- Secure access, monitor operation, test behavior, and document costs.

## Proposed solution
**Option A:** EC2 Linux + dedicated EBS application volume + private S3 document bucket, IAM role, Systems Manager for administration, CloudWatch, EBS snapshots.  
**Option B:** Serverless rewrite with API Gateway + Lambda + DynamoDB + S3.

**Proposed selection: Option A** because the requirements describe *migration of an existing application*, limited workload, and emphasis on infrastructure and recovery. This is an architectural decision under review, **not evidence of completed deployment**.

## Repository map
| Folder | Contents |
| --- | --- |
| `requirements/` | Business/technical requirements and assumptions |
| `architecture/` | Two options, diagrams, comparison, service choices |
| `decisions/` | Four Architecture Decision Records |
| `terraform/` | Initial AWS infrastructure code |
| `application/` | Sample application placeholder (Week 3) |
| `tests/` | Test matrix and evidence checklist |
| `progress/` | Weekly goals, status and open risks |
| `presentation/` | Final presentation (Week 4) |

## Progress & evidence
| Milestone | Status |
| --- | --- |
| Week 1 requirements & alternatives | **Drafted — review needed** |
| Week 2 comparison and architecture decision | **Drafted — review needed** |
| Week 2 Terraform infrastructure | **Code prepared — not deployed** |
| Week 3 working application, persistence, backup/recovery, monitoring | **Pending** |
| Week 4 Well-Architected, costs, final tests and presentation | **Pending** |

## Safety and cost
Do not commit credentials, local Terraform state or real customer documents. This is a controlled prototype: EC2 has **no inbound security-group rules** and is intended for administrative access via SSM. Secure employee-facing application access/authentication remains to be designed and must **not** be represented as production-ready. An EC2 instance, EBS volume and public IPv4 address may generate costs. Always check the active AWS billing plan and destroy resources when they are no longer needed.

## Infrastructure commands (run only after reviewing cost/security)
```bash
cd terraform
terraform fmt -recursive
terraform init
terraform validate
terraform plan
# Apply only after reviewing the plan and your AWS account/region
terraform apply
```

Final application deployment and backup/recovery commands will be documented after implementation and actual tests. The final architecture diagram must reflect what was truly built.
