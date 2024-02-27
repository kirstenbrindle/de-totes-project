
resource "aws_lambda_function" "lambda2" {
  function_name    = var.lambda2
  role             = aws_iam_role.L2_lambda_role.arn
  handler          = "transform_handler2.lambda_handler"
  runtime          = "python3.10"
  s3_bucket        = aws_s3_bucket.code_bucket.id
  s3_key           = "lambda2/lambda2.zip"
  source_code_hash = data.archive_file.lambda2.output_base64sha256
  architectures = ["arm64"]
  timeout = 120 
  memory_size = 256
  layers = ["arn:aws:lambda:eu-west-2:336392948345:layer:AWSSDKPandas-Python310-Arm64:11", aws_lambda_layer_version.lambda2_layer_dependencies.arn] 
  }

resource "aws_lambda_layer_version" "lambda2_layer_dependencies" {
  layer_name          = "lambda_layer2"
  s3_bucket           = aws_s3_bucket.code_bucket.id
  s3_key              = aws_s3_object.lambda2_layer_zip.key
  compatible_runtimes = ["python3.10"]
  source_code_hash    = base64sha256(filebase64("${path.module}/../aws_utils/layer_code2.zip"))
}

resource "aws_lambda_permission" "allow_s3" {
  action = "lambda:InvokeFunction"
  function_name = aws_lambda_function.lambda2.function_name
  principal = "s3.amazonaws.com"
  source_arn = aws_s3_bucket.ingestion_bucket.arn
  source_account = data.aws_caller_identity.current.account_id
}
