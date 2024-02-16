# First, create policy document
# Second, create policy
# Third, attach correct policy to IAM role for L1

# Creating L1 IAM Role...
resource "aws_iam_role" "L1_lambda_role" {
  name = "L1_lambda_role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Sid    = ""
        Principal = {
          Service = "lambda.amazonaws.com"
        }
      },
    ]
  })
}

# Creating S3 Ingestion bucket policy document ...
data "aws_iam_policy_document" "s3_L1_document" {
  statement {
    actions = [
        "s3:PutObject",
        "s3:ListBucket"
        ] 
    resources = [
      "${aws_s3_bucket.ingestion_bucket.arn}/*", 
      "${aws_s3_bucket.code_bucket.arn}/*"
    ]
  }
}

# Creating S3 Ingestion bucket policy ...
resource "aws_iam_policy" "s3_L1_policy" {
  name_prefix = "s3-L1-policy-de-totes-project-"
  policy      = data.aws_iam_policy_document.s3_L1_document.json
}

# Attaching S3 ingestion policy to L1 IAM Role ...
resource "aws_iam_role_policy_attachment" "L1_S3_policy_attachment" {
  role       = aws_iam_role.L1_lambda_role.name
  policy_arn = aws_iam_policy.s3_L1_policy.arn
}

#Creating Cloudwatch policy document...
data "aws_iam_policy_document" "L1_cloudwatch_document" {
  statement {

    actions = ["logs:CreateLogGroup"]

    resources = [
      "arn:aws:logs:${data.aws_region.current.name}:${data.aws_caller_identity.current.account_id}:*"
    ]
    effect = "Allow"
  }

  statement {

    actions = ["logs:CreateLogStream", "logs:PutLogEvents"]

    resources = [ # Please change below according to L1 function name 
      "arn:aws:logs:${data.aws_region.current.name}:${data.aws_caller_identity.current.account_id}:log-group:/aws/lambda/lambda1:*"
    ]
  }
}

# Creating Cloudwatch policy ...
resource "aws_iam_policy" "L1_cloudwatch_policy" {
  name_prefix = "L1-cloudwatch-policy-de-totes-project-"
  policy      = data.aws_iam_policy_document.L1_cloudwatch_document.json
}

# Attaching Cloudwatch Policy to L1 IAM Role ...
resource "aws_iam_role_policy_attachment" "L1_cloudwatch_policy_attachment" {
  role       = aws_iam_role.L1_lambda_role.name
  policy_arn = aws_iam_policy.L1_cloudwatch_policy.arn
}


# making eventbridge role
resource "aws_iam_role" "L1_eventbridge_role" {
  name = "L1_eventbridge_role"
  assume_role_policy = jsonencode({

    "Version" : "2012-10-17",
    "Statement" : [
      {
        "Effect" : "Allow",
        "Principal" : {
          "Service" : "scheduler.amazonaws.com"
        },
        "Action" : "sts:AssumeRole"
      },
    ]
  })
}

