data "aws_availability_zones" "available" {
  state = "available"
}

resource "aws_vpc" "main" {
  cidr_block           = var.vpc_cidr
  enable_dns_support   = true
  enable_dns_hostnames = true
  tags = { Name = "${var.project_name}-vpc" }
}
resource "aws_internet_gateway" "igw" {
  vpc_id = aws_vpc.main.id
  tags   = { Name = "${var.project_name}-igw" }
}
resource "aws_subnet" "app" {
  vpc_id                  = aws_vpc.main.id
  cidr_block              = var.subnet_cidr
  availability_zone       = data.aws_availability_zones.available.names[0]
  map_public_ip_on_launch = true
  tags                    = { Name = "${var.project_name}-app-subnet" }
}
resource "aws_route_table" "public" {
  vpc_id = aws_vpc.main.id
  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.igw.id
  }
  tags = { Name = "${var.project_name}-public-rt" }
}
resource "aws_route_table_association" "app" {
  subnet_id      = aws_subnet.app.id
  route_table_id = aws_route_table.public.id
}
resource "aws_security_group" "app" {
  name_prefix = "${var.project_name}-app-"
  description = "No inbound access; SSM administration over outbound TLS"
  vpc_id      = aws_vpc.main.id
  tags        = { Name = "${var.project_name}-app-sg" }
}
resource "aws_vpc_security_group_egress_rule" "https" {
  security_group_id = aws_security_group.app.id
  cidr_ipv4         = "0.0.0.0/0"
  from_port         = 443
  to_port           = 443
  ip_protocol       = "tcp"
  description       = "TLS outbound for AWS services, SSM, package downloads"
}
