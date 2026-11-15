output "instance_id" {
  description = "EC2 instance ID (use with AWS Systems Manager)."
  value       = aws_instance.app.id
}
output "document_bucket" {
  description = "Private S3 bucket for uploaded document objects."
  value       = aws_s3_bucket.documents.bucket
}
output "data_volume_id" {
  description = "Dedicated encrypted EBS volume; still requires filesystem/mount setup."
  value       = aws_ebs_volume.app_data.id
}
output "availability_zone" {
  value = aws_subnet.app.availability_zone
}
output "vpc_id" {
  value = aws_vpc.main.id
}
