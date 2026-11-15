resource "aws_s3_bucket" "documents" {
  bucket_prefix = "${var.project_name}-docs-"
  force_destroy = false
  tags          = { Name = "${var.project_name}-documents" }
}
resource "aws_s3_bucket_public_access_block" "documents" {
  bucket                  = aws_s3_bucket.documents.id
  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}
resource "aws_s3_bucket_versioning" "documents" {
  bucket = aws_s3_bucket.documents.id
  versioning_configuration {
    status = "Enabled"
  }
}
resource "aws_s3_bucket_server_side_encryption_configuration" "documents" {
  bucket = aws_s3_bucket.documents.id
  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}
resource "aws_ebs_volume" "app_data" {
  availability_zone = aws_subnet.app.availability_zone
  size              = 8
  type              = "gp3"
  encrypted         = true
  tags              = { Name = "${var.project_name}-app-data" }
}
resource "aws_volume_attachment" "app_data" {
  device_name = "/dev/sdf"
  volume_id   = aws_ebs_volume.app_data.id
  instance_id = aws_instance.app.id
}
