#This  is the first bucket for ingestion data from totesys


resource "aws_s3_bucket" "ingestion_bucket" {
    bucket_prefix = "ingestion-bucket-de-totes-project-"
}
#Fill the bucket with correct data
resource "aws_s3_object" "lambda_ingestion_data" {
    bucket = aws_s3_bucket.ingestion_bucket.id
    key = "NAME OF CODE/function.zip"
    source = "${path.module}/../function.zip"
}

