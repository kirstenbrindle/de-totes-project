# #Uploading the L3 code zip to the code bucket
# resource "aws_s3_object" "L3_object" {
#   bucket      = aws_s3_bucket.code_bucket.id # refers to code bucket made in s3.tf
#   key         = "lambda3/lambda3.zip"
#   source      = "${path.module}/../lambda3.zip"
#   source_hash = filemd5("${path.module}/../lambda3.zip")
# }


# #Uploading the L3 layer zip to the code bucket
# resource "aws_s3_object" "lambda3_layer_zip" {
#   bucket      = aws_s3_bucket.code_bucket.id
#   key         = "processed_code_layer/layer_code3.zip"
#   source      = "${path.module}/../aws_utils/layer_code3.zip"
#   source_hash = filemd5("${path.module}/../aws_utils/layer_code3.zip")
# }


# resource "aws_s3_bucket_notification" "bucket_notification_L3" {
#   bucket = aws_s3_bucket.processed_bucket.id

#   lambda_function {
#     lambda_function_arn = aws_lambda_function.lambda3.arn
#     events              = ["s3:ObjectCreated:*"]
#   }

#   depends_on = [aws_lambda_permission.allow_s3_L3]
# }
