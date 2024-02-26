# Creating L2 IAM Role...
resource "aws_iam_role" "L2_lambda_role" {
  name = "L2_lambda_role"
  assume_role_policy = jsonencode(
    {
      "Version" : "2012-10-17",
      "Statement" : [
        {
          "Effect" : "Allow",
          "Action" : [
            "sts:AssumeRole"
          ],
          "Principal" : {
            "Service" : [
              "lambda.amazonaws.com"
            ]
          }
        }
      ]
  })
}

# Creating S3 Processed bucket policy document ...
data "aws_iam_policy_document" "s3_L2_document" {
  statement {
    actions = [
      "s3:ListBucket"
    ]
    resources = [
      "${aws_s3_bucket.processed_bucket.arn}",
      "${aws_s3_bucket.ingestion_bucket.arn}",
      "${aws_s3_bucket.code_bucket.arn}"
    ]
    effect = "Allow"
  }
  statement {
    actions = [
      "s3:*Object"
    ]
    resources = [
      "${aws_s3_bucket.processed_bucket.arn}/*",
      "${aws_s3_bucket.ingestion_bucket.arn}/*",
      "${aws_s3_bucket.code_bucket.arn}/*"
    ]
    effect = "Allow"
  }
  statement {
    actions = [
      "s3:ListAllMyBuckets"
    ]
    resources = [
      "arn:aws:s3:::*"

    ]
    effect = "Allow"
  }
}

# Creating S3 Processed bucket policy ...
resource "aws_iam_policy" "s3_L2_policy" {
  name_prefix = "s3-L2-policy-de-totes-project-"
  policy      = data.aws_iam_policy_document.s3_L2_document.json
}

# Attaching S3 Processed policy to L2 IAM Role ...
resource "aws_iam_role_policy_attachment" "L2_S3_policy_attachment" {
  role       = aws_iam_role.L2_lambda_role.name
  policy_arn = aws_iam_policy.s3_L2_policy.arn
}

#Creating Cloudwatch policy document for L2...
data "aws_iam_policy_document" "L2_cloudwatch_document" {
  statement {
    actions = ["logs:CreateLogGroup"]

    resources = [
      "arn:aws:logs:eu-west-2:${data.aws_caller_identity.current.account_id}:*"
    ]

    effect = "Allow"
  }

  statement {
    actions = ["logs:CreateLogStream", "logs:PutLogEvents"]

    resources = [
      "arn:aws:logs:eu-west-2:${data.aws_caller_identity.current.account_id}:log-group:/aws/lambda/${var.lambda2}:*"
    ]
  }
}

# Creating Cloudwatch policy ...
resource "aws_iam_policy" "L2_cloudwatch_policy" {
  name_prefix = "L2-cloudwatch-policy-de-totes-project-"
  policy      = data.aws_iam_policy_document.L2_cloudwatch_document.json
}

# Attaching Cloudwatch Policy to L2 IAM Role ...
resource "aws_iam_role_policy_attachment" "L2_cloudwatch_policy_attachment" {
  role       = aws_iam_role.L2_lambda_role.name
  policy_arn = aws_iam_policy.L2_cloudwatch_policy.arn
}