# DocuWorks | AWS Document Management Platform

**DCI Final Project — Implementation / Cloud Infrastructure**  
**AWS Region:** `eu-central-1` (deployed)

**Status (2026-11-15):** Working EC2 document workflow deployed and tested. EBS snapshot completed; recovery, monitoring and infrastructure automation remain open.

## Business problem
A small company (10–20 employees) operates an internal document-management application on one physical server. Uploaded documents and application data reside together, backups are manual, and server failure interrupts availability. The company needs a cost-conscious, secure AWS migration.

## Practical context: industrial document workflows
The demo uses **synthetic maintenance reports and quality-inspection records** from a production-line scenario. This choice is deliberate: operational records are useful only when the original file, its processing status and its history remain available after routine restarts or incidents. Typical examples include a sensor replacement report, a pressure fluctuation recorded during startup or a quality-control release note.

The design reflects experience with automated production environments: reliable operations, troubleshooting and traceable handovers matter more than adding unnecessary cloud services. DocuWorks remains a **document-management platform**, not an industrial control system. The sample data is fictional and is not taken from a former employer.

The technical separation follows that problem: **S3 preserves uploaded files**, **EBS stores mutable SQLite metadata**, and **EC2 runs the application**. SSM provides restricted administrative/demo access without opening SSH or HTTP inbound. A single-instance design is intentionally low-complexity but does not provide high availability.

## Project objectives
- Design and compare **two** AWS architecture options.
- Deploy a small Linux application environment using **Terraform**.
- Keep uploaded documents separately from the application environment.
- Demonstrate persistent application data and backup/recovery.
- Secure access, monitor operation, test behavior, and document costs.

## Proposed solution
**Option A:** EC2 Linux + dedicated EBS application volume + private S3 document bucket, IAM role, Systems Manager for administration, CloudWatch, EBS snapshots.  
**Option B:** Serverless rewrite with API Gateway + Lambda + DynamoDB + S3.

**Implemented selection: Option A** because the requirements describe *migration of an existing application*, limited workload, and emphasis on infrastructure and recovery. The EC2/EBS/S3 foundation was deployed with Terraform on 2026-11-15. Documented trade-offs are still subject to review.

## Repository map
| Folder | Contents |
| --- | --- |
| `requirements/` | Business/technical requirements and assumptions |
| `architecture/` | Two options, diagrams, comparison, service choices |
| `decisions/` | Four Architecture Decision Records |
| `terraform/` | Initial AWS infrastructure code |
| `application/` | Working Flask document register, S3 integration and SQLite metadata |
| `tests/` | Test matrix and evidence checklist |
| `progress/` | Weekly goals, status and open risks |
| `presentation/` | Final presentation (Week 4) |

## Progress & evidence
| Milestone | Status |
| --- | --- |
| Week 1 requirements & alternatives | **Drafts present; diagrams and instructor review pending** |
| Week 2 architecture choice and ADRs | **Comparison and 4 ADR drafts present; final diagram pending** |
| Week 2 Terraform infrastructure | **18 resources deployed successfully in eu-central-1** |
| Week 3 application and persistent storage | **Working: EC2 / Gunicorn / systemd, S3 files, SQLite on EBS, restart tested** |
| Week 3 backup and recovery | **EBS snapshot completed; recovery not tested** |
| Week 3 monitoring and logging | **Local journal logs available; CloudWatch integration pending** |
| Week 4 security, cost, reproducibility, presentation | **Pending evaluation and completion** |

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

Application runtime and EBS mount were configured manually on the instance, not yet automated via Terraform/user_data. Snapshot `snap-0af6e7490c0fcb177` completed on 2026-11-15; no restore test yet. See `progress/2026-11-15.md` and `tests/test-plan.md` for verified evidence. The final architecture diagram must reflect only what is actually deployed.
