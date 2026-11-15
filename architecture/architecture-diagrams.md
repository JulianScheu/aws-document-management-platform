# Architecture alternatives — draft diagrams

Diagrams describe **design options**, not an existing AWS deployment.

## Option A — EC2 / EBS / S3

```mermaid
flowchart TD
  employee[Authorized employee] --> access[Secure application access - to be designed]
  subgraph region[AWS Region eu-central-1]
    subgraph vpc[VPC]
      access --> ec2[EC2 Linux application]
      ec2 --> ebs[EBS application-data volume]
    end
    ec2 --> s3[S3 private document bucket]
    ec2 --> cw[CloudWatch]
    iam[IAM instance role] -. grants .-> ec2
    ebs -. backup .-> snap[EBS Snapshot]
  end
```

## Option B — Serverless redesign

```mermaid
flowchart TD
  staff[Authorized employee] --> auth[Authentication/Authorization]
  auth --> api[API Gateway]
  api --> lambda[Lambda document API]
  lambda --> s3[S3 private documents]
  lambda --> dynamo[DynamoDB application metadata]
  lambda --> cw[CloudWatch]
```

## Final architecture diagram
**Not final yet.** Replace this section with a diagram of actual deployed resources, accurate subnets/security boundaries, storage and recovery flow once Week 3 implementation is complete.
