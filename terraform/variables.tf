variable "aws_region" {
  description = "AWS Region for all DocuWorks resources."
  type        = string
  default     = "eu-central-1"
}
variable "project_name" {
  description = "Resource name prefix."
  type        = string
  default     = "dci-docuworks"
}
variable "instance_type" {
  description = "EC2 type; verify account pricing and architecture compatibility."
  type        = string
  default     = "t3.micro"
}
variable "vpc_cidr" {
  type    = string
  default = "10.20.0.0/16"
}
variable "subnet_cidr" {
  type    = string
  default = "10.20.1.0/24"
}
