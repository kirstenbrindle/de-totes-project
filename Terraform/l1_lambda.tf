resource "aws_lambda_function" "lambda1" {
  function_name    = var.lambda1
  role             = aws_iam_role.L1_lambda_role.arn
  handler          = "extract_handler1.lambda_handler"
  runtime          = "python3.10"
  s3_bucket        = aws_s3_bucket.code_bucket.id
  s3_key           = "lambda1/lambda1.zip"
  source_code_hash = data.archive_file.lambda1.output_base64sha256
  architectures = ["arm64"]
  timeout = 120
  memory_size = 256
  environment {
    variables = {
      S3_ingestion_bucket = "${aws_s3_bucket.ingestion_bucket.id}"
    }
  }
  layers = ["arn:aws:lambda:eu-west-2:336392948345:layer:AWSSDKPandas-Python310-Arm64:11", aws_lambda_layer_version.lambda_layer_dependencies.arn] 
}

resource "aws_lambda_layer_version" "lambda_layer_dependencies" {
  layer_name          = "lambda_layer1"
  s3_bucket           = aws_s3_bucket.code_bucket.id
  s3_key              = aws_s3_object.lambda_layer_zip.key
  compatible_runtimes = ["python3.10"]
  source_code_hash    = base64sha256(filebase64("${path.module}/../aws_utils/layer_code1.zip"))
}
