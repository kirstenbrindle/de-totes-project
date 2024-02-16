# First, create policy document
# Second, create policy
# Third, attach correct policy to IAM role for L1

# Creating L1 IAM Role...
# resource "aws_iam_role" "L1_role" {
#   name = "L1_Role"
#   assume_role_policy = jsonencode({
#     Version = "2012-10-17"
#     Statement = [
#       {
#         Action = "sts:AssumeRole"
#         Effect = "Allow"
#         Sid    = ""
#         Principal = {
#           Service = "lambda.amazonaws.com"
#         }
#       },
#     ]
#   })
# }

# Creating S3 Ingestion bucket policy document ...
# data "aws_iam_policy_document" "s3_ingestion_document" {
#   statement {
#     actions = ["s3:PutObject"] # this put things in our ingestion bucket -> do we also need permission to list objects? (get file names)
#     resources = [
#       "${aws_s3_bucket.ingestion_bucket.arn}/*", 
#       "${aws_s3_bucket.code_bucket.arn}/*",
#     ]
#   }
# }

# Creating S3 Ingestion bucket policy ...
# resource "aws_iam_policy" "s3_ingestion_policy" {
#   name_prefix = "s3-ingestion-policy-de-totes-project-"
#   policy      = data.aws_iam_policy_document.s3_ingestion_document.json
# }

# Attaching S3 ingestion policy to L1 IAM Role ...
# resource "aws_iam_role_policy_attachment" "L1_S3_ingestion_policy_attachment" {
#   role       = aws_iam_role.L1_role.name
#   policy_arn = aws_iam_policy.s3_ingestion_policy.arn
# }


#Creating Cloudwatch policy document...
# data "aws_iam_policy_document" "L1_cloudwatch_document" {
#   statement {

#     actions = ["logs:CreateLogGroup"]

#     resources = [
#       "arn:aws:logs:${data.aws_region.current.name}:${data.aws_caller_identity.current.account_id}:*"
#     ]
#     effect = "Allow"
#   }

#   statement {

#     actions = ["logs:CreateLogStream", "logs:PutLogEvents"]

#     resources = [ # Please change below according to L1 function name 
#       "arn:aws:logs:${data.aws_region.current.name}:${data.aws_caller_identity.current.account_id}:log-group:/aws/lambda/L1_FUNCTION_NAME:*"
#     ]
#   }
# }

# Creating Cloudwatch policy ...
# resource "aws_iam_policy" "L1_cloudwatch_policy" {
#   name_prefix = "L1-cloudwatch-policy-de-totes-project-"
#   policy      = data.aws_iam_policy_document.L1_cloudwatch_document.json
# }

# Attaching Cloudwatch Policy to L1 IAM Role ...
# resource "aws_iam_role_policy_attachment" "L1_cloudwatch_policy_attachment" {
#   role       = aws_iam_role.L1_role.name
#   policy_arn = aws_iam_policy.L1_cloudwatch_policy.arn
# }


# making eventbridge role
# resource "aws_iam_role" "eventbridge_l1" {
#   name = "eventbridge_l1"
#   assume_role_policy = jsonencode({

#     "Version" : "2012-10-17",
#     "Statement" : [
#       {
#         "Effect" : "Allow",
#         "Principal" : {
#           "Service" : "scheduler.amazonaws.com"
#         },
#         "Action" : "sts:AssumeRole"
#       },
#     ]
#   })
# }

