#This  is the first bucket for ingestion data from totesys

resource "aws_s3_bucket" "ingestion_bucket" {
  bucket_prefix = "ingestion-bucket-de-totes-project-"
}


#This bucket is created for python code

resource "aws_s3_bucket" "code_bucket" {
  bucket_prefix = "code-bucket-de-totes-project-"
}

#Resource to upload the zipped code to the code bucket

# resource "aws_s3_object" "first_lambda_object" {
#   bucket = aws_s3_bucket.code_bucket.id
#   key    = "NAME OF CODE/function.zip"
#   source = "${path.module}/../function.zip"
# }
