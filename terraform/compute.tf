data "aws_ssm_parameter" "amazon_linux_2023" {
  name = "/aws/service/ami-amazon-linux-latest/al2023-ami-kernel-default-x86_64"
}
resource "aws_instance" "app" {
  ami                         = data.aws_ssm_parameter.amazon_linux_2023.value
  instance_type               = var.instance_type
  subnet_id                   = aws_subnet.app.id
  vpc_security_group_ids      = [aws_security_group.app.id]
  iam_instance_profile        = aws_iam_instance_profile.app.name
  associate_public_ip_address = true
  metadata_options {
    http_tokens = "required"
  }
  root_block_device {
    volume_size           = 12
    volume_type           = "gp3"
    encrypted             = true
    delete_on_termination = true
  }
  tags = { Name = "${var.project_name}-app" }
  depends_on = [
    aws_route_table_association.app,
    aws_iam_role_policy_attachment.ssm
  ]
}
