provider "aws" {
  region = var.aws_region
  default_tags {
    tags = {
      Project     = "dci-docuworks"
      Environment = "training"
      ManagedBy   = "Terraform"
    }
  }
}
