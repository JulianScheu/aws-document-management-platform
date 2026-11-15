# Assumptions and constraints

## Explicitly supplied by assignment
- Four-week project; individual or team of two.
- Personal AWS account; Free Tier / credits are account-dependent.
- A small company with 10–20 employees, 50–100 documents/day, average below 10 MB.
- Final AWS infrastructure **must** be provisioned using Terraform.
- Two architecture alternatives, 3–5 ADRs, working application, backup/recovery, security, monitoring, tests, GitHub and final presentation.

## Assumptions (must be validated)
- A lightweight sample application can represent the existing workload.
- The sample application can run on Linux EC2.
- The initial deployment can use one AWS Region (`eu-central-1`).
- A small single-AZ prototype is acceptable if limitations are openly documented.
- Administrative access for the demo can use SSM; a separate employee authentication and secure endpoint design is needed for production.
- Synthetic sample documents will be used, never actual customer data.
- Availability targets, recovery targets, account limits, and specific employee login requirements are not defined in the scenario; they must not be invented as business facts.

## Risks
- Compressed schedule and delayed project start.
- Personal AWS charges if instances/storage/public IPs remain running.
- EBS volume must be mounted and restored deliberately; Terraform resource creation alone does not prove app data persistence.
- Staff-facing authentication is not provided by SSM-only administrative access.
