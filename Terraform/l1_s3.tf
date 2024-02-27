resource "aws_s3_bucket" "ingestion_bucket" {
  bucket_prefix = "ingestion-bucket-de-totes-project-"
}

resource "aws_s3_bucket" "code_bucket" {
  bucket_prefix = "code-bucket-de-totes-project-"
}

resource "aws_s3_object" "L1_object" {
  bucket = aws_s3_bucket.code_bucket.id
  key    = "lambda1/lambda1.zip"
  source = "${path.module}/../lambda1.zip"
  source_hash = filemd5("${path.module}/../lambda1.zip")
}
