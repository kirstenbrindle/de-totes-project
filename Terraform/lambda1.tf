  
  
  environment {
    variables = {
      S3_ingestion_bucket = "${aws_s3_bucket.s3_ingestion_bucket.id}"
    }