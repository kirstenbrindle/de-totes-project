#Creating the 'processed' bucket for L2 ...
resource "aws_s3_bucket" "processed_bucket" {
  bucket_prefix = "processed-bucket-de-totes-project-"
}

#Uploading the L2 code zip to the code bucket
resource "aws_s3_object" "L2_object" {
  bucket      = aws_s3_bucket.code_bucket.id # refers to code bucket made in s3.tf
  key         = "lambda2/lambda2.zip"
  source      = "${path.module}/../lambda2.zip"
  source_hash = filemd5("${path.module}/../lambda2.zip")
}

#Uploading the L2 layer zip to the code bucket
resource "aws_s3_object" "lambda2_layer_zip" {
  bucket      = aws_s3_bucket.code_bucket.id
  key         = "processed_code_layer/layer_code2.zip"
  source      = "${path.module}/../aws_utils/layer_code2.zip"
  source_hash = filemd5("${path.module}/../aws_utils/layer_code2.zip")
}
# The L1 equivalent of ^^this^^ is kept in lambda1_layers.tf but decided to put
# the L2 layer zip in with the other S3 resources

# I have created the layer_code2 folder in aws_utils but it currently only contains
# the basic dependencies like scramp and dateutil (none of our utils funcs)

# Creating the bucket notification...
resource "aws_s3_bucket_notification" "bucket_notification" {
  bucket = aws_s3_bucket.ingestion_bucket.id

  lambda_function {
    lambda_function_arn = aws_lambda_function.lambda2.arn
    events              = ["s3:ObjectCreated:*"]
  }

  depends_on = [aws_lambda_permission.allow_s3]
}

# ^^the above is copied from the s3_file_reader
