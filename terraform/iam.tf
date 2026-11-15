data "aws_iam_policy_document" "ec2_trust" {
  statement {
    actions = ["sts:AssumeRole"]
    principals {
      type        = "Service"
      identifiers = ["ec2.amazonaws.com"]
    }
  }
}
resource "aws_iam_role" "app" {
  name_prefix        = "${var.project_name}-ec2-"
  assume_role_policy = data.aws_iam_policy_document.ec2_trust.json
}
resource "aws_iam_role_policy_attachment" "ssm" {
  role       = aws_iam_role.app.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore"
}

data "aws_iam_policy_document" "documents_access" {
  statement {
    sid       = "ListDocumentBucket"
    actions   = ["s3:ListBucket"]
    resources = [aws_s3_bucket.documents.arn]
  }
  statement {
    sid       = "ReadWriteDocumentObjects"
    actions   = ["s3:GetObject", "s3:PutObject"]
    resources = ["${aws_s3_bucket.documents.arn}/*"]
  }
}
resource "aws_iam_role_policy" "documents_access" {
  name   = "documents-bucket-access"
  role   = aws_iam_role.app.id
  policy = data.aws_iam_policy_document.documents_access.json
}
resource "aws_iam_instance_profile" "app" {
  name_prefix = "${var.project_name}-ec2-"
  role        = aws_iam_role.app.name
}
