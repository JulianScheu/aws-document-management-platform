# Option B — Serverless application redesign

## Overview
A redesigned API exposes document operations through API Gateway. Lambda implements request handling, S3 stores document objects, and DynamoDB stores application metadata. IAM and CloudWatch cover access and observability. Access control must be specified for employees.

## Data flow
Authenticated employee → API Gateway → Lambda → S3 (objects) + DynamoDB (metadata).

## Benefits
- Managed, event-driven components with little server administration.
- On-demand resource scaling for variable workloads.
- Compute cost can be low at small volumes.

## Weaknesses and risks
- The existing server application likely needs refactoring or rewriting.
- Adds API and application development work rather than testing a simple migration.
- Different data-recovery design, including backup/PITR considerations for metadata.
- More implementation uncertainty under a shortened deadline.
