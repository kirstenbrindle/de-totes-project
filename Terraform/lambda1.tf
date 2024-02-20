# L1 lambda function resource

resource "aws_lambda_function" "lambda1" {
  function_name = var.lambda1
  role          = aws_iam_role.L1_lambda_role.arn
  handler       = "lambda1.lambda_handler"
  runtime       = "python3.10"
  s3_bucket     = aws_s3_bucket.code_bucket.id
  s3_key        = "lambda1/lambda1.zip"
  source_code_hash = "${data.archive_file.lambda1.output_base64sha256}"
  environment {
    variables = {
      S3_ingestion_bucket = "${aws_s3_bucket.ingestion_bucket.id}"
    }
  }
  layers = ["arn:aws:lambda:eu-west-2:336392948345:layer:AWSSDKPandas-Python311:8", aws_lambda_layer_version.lambda_layer.arn]
}


# do we need this? as in previous tasks, the bucket has triggered the lambda but here, it is on a schedule
resource "aws_lambda_permission" "allow_eventbridge" {
  action         = "lambda:InvokeFunction"
  function_name  = aws_lambda_function.lambda1.function_name
  principal      = "events.amazonaws.com"
  source_arn     = aws_scheduler_schedule.L1_scheduler.arn
  source_account = data.aws_caller_identity.current.account_id
}

