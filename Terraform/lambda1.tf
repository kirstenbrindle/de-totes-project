  
  
  # environment {
  #   variables = {
  #     S3_ingestion_bucket = "${aws_s3_bucket.s3_ingestion_bucket.id}"
  #   }

# L1 lambda function resource

# resource "aws_lambda_function" "L1_injestion" {
#   function_name = var.lambda_name -> TBC
#   role          = aws_iam_role.L1_role.arn
#   handler       = "lambda1.lambda_handler" -> lambda file name TBC
#   runtime       = "python3.11"
#   s3_bucket     = aws_s3_bucket.code_bucket.id
#   s3_key        = "L1_injestion/function.zip" -> file path/name TBC
# }


# do we need this? as in previous tasks, the bucket has triggered the lambda but here, it is on a schedule
# resource "aws_lambda_permission" "allow_s3" {
#   action         = "lambda:InvokeFunction"
#   function_name  = aws_lambda_function.L1_injestion.function_name
#   principal      = "s3.amazonaws.com"
#   source_arn     = aws_s3_bucket.injestion_bucket.arn
#   source_account = data.aws_caller_identity.current.account_id
# }