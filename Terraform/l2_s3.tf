resource "aws_s3_bucket" "processed_bucket" {
  bucket_prefix = "processed-bucket-de-totes-project-"
}

resource "aws_s3_object" "L2_object" {
  bucket      = aws_s3_bucket.code_bucket.id
  key         = "lambda2/lambda2.zip"
  source      = "${path.module}/../lambda2.zip"
  source_hash = filemd5("${path.module}/../lambda2.zip")
}

resource "aws_s3_object" "lambda2_layer_zip" {
  bucket      = aws_s3_bucket.code_bucket.id
  key         = "processed_code_layer/layer_code2.zip"
  source      = "${path.module}/../aws_utils/layer_code2.zip"
  source_hash = filemd5("${path.module}/../aws_utils/layer_code2.zip")
}

resource "aws_s3_bucket_notification" "bucket_notification" {
  bucket = aws_s3_bucket.ingestion_bucket.id

  lambda_function {
    lambda_function_arn = aws_lambda_function.lambda2.arn
    events              = ["s3:ObjectCreated:*"]
  }

  depends_on = [aws_lambda_permission.allow_s3]
}
