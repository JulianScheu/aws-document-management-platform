# Option A — EC2 + EBS + S3

## Overview
A Linux application runs on one EC2 instance inside a VPC. Application state uses an independently managed EBS data volume. Uploaded documents reside in a private S3 bucket and are accessed using an EC2 IAM role. CloudWatch supports observability. EBS snapshots provide a testable recovery path.

## Data flow
Authorized client → secured application entry → EC2 application → **EBS** (application data) + **S3** (document objects).

## Benefits
- Familiar server migration pattern with limited refactoring.
- Directly demonstrates Terraform, Linux, networking, IAM, block/object storage and backups.
- Easier to keep small and understandable.

## Weaknesses and risks
- EC2 is a single point of failure; this design does **not** promise automatic failover.
- EBS is Availability-Zone specific; the replacement instance must access an appropriate volume in the same AZ or data must be restored into a new volume.
- OS security updates and application processes need ongoing maintenance.
- SSM admin connectivity is not a normal end-user application access solution; production employee access and authentication require additional controls.

## Prototype access strategy
Initial Terraform opens **no inbound Security Group rules**. Remote administrative sessions can use AWS Systems Manager Session Manager. Actual user-facing secure HTTPS/authentication remains an identified gap, not a completed feature.
