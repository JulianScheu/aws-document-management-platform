# Business requirements

## Current state
DocuWorks runs a small internal document application on a single physical server. The application, application data and uploaded documents share that server. Backup is manual, infrastructure changes are manual and a server outage may interrupt employee access. The company wants a small, cost-conscious first AWS version rather than a complex enterprise system.

## Given workload
- Employees: **10–20**
- Documents: **50–100 per day**
- Average document size: **less than 10 MB**
- App load: **low to moderate**
- Expected change: gradual growth

## Functional requirements
| ID | Business requirement | Acceptance evidence |
| --- | --- | --- |
| BR-01 | Host the existing application or a suitable sample on AWS | Working demo |
| BR-02 | Employees can access the application over a network | Successful authorized request |
| BR-03 | Users can upload documents | Demonstrate upload |
| BR-04 | Users can retrieve documents | Demonstrate retrieval |
| BR-05 | Application data persists across restart/replacement | Persistence test |
| BR-06 | Document files can be stored separately from application compute | Document location and access shown |
| BR-07 | Important data is backed up and restorable | Backup and **actual** restore |
| BR-08 | Admin access is restricted | Deny test/permissions review |
| BR-09 | Monitoring and logging exist | Logs/metrics evidence |
| BR-10 | Infrastructure is reproducible using Terraform | Init/plan/apply/destroy evidence |

## Definition of success
A functioning sample document workflow, reproducible infrastructure, documented security boundaries, a successful persistence test, and at least **one demonstrated recovery operation**.
