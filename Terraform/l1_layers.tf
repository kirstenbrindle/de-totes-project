locals {
  layer_path        = "lambda1_layer"
  layer_zip_name    = "lambda1_layer.zip"
  layer_name        = "lambda1_dep_layer"
  requirements_name = "requirements.txt"
  requirements_path = "${path.module}/../src/layers/L1-layer/requirements.txt"
}

resource "aws_s3_object" "lambda_layer_zip" {
  bucket = aws_s3_bucket.code_bucket.id
  key    = "ingestion_code_layer/layer_code1.zip"
  source = "${path.module}/../aws_utils/layer_code1.zip"
  source_hash = filemd5("${path.module}/../aws_utils/layer_code1.zip")
}


