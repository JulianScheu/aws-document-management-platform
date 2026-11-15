# Terraform foundation — prepared but NOT deployed

Creates:
- One VPC / one subnet / Internet Gateway / routing
- Security group **without inbound rules** (outbound HTTPS)
- Amazon Linux 2023 EC2 with SSM instance role
- A separate gp3 EBS data volume in the same Availability Zone, attached to EC2
- Private S3 bucket with public access block, encryption and versioning
- IAM role with scoped S3 access

**Only the foundation is implemented.** The data volume is NOT formatted or mounted automatically, the sample document app is NOT deployed, and there is no staff-facing HTTPS/authentication. These are the next steps.

## Prerequisites
- Terraform CLI installed
- AWS CLI authenticated with permitted IAM role/user
- Personal AWS account, checked billing and budget alerts
- Available service quotas and EC2 instance type
- Region `eu-central-1` unless changed

## Commands
```bash
aws sts get-caller-identity
terraform fmt -recursive
terraform init
terraform validate
terraform plan
# Review plan and costs first
terraform apply
terraform output
```

## Safety
EC2, EBS, public IPv4 and snapshots can incur cost. Do not leave resources on unnecessarily. No SSH port is open. Use **AWS Systems Manager Session Manager** after verifying the instance is managed. A public IP allows outbound internet via Internet Gateway but does not make the app reachable because inbound is blocked.

## Cleanup
First remove test S3 objects and previous object versions, then run `terraform destroy`. Verify that the EBS volume, instance, snapshots, public IPv4, and S3 objects are gone. S3 may block destroy if the bucket still contains objects; this is intentional to prevent accidental data loss. Do not delete actual records.
