# # Creating L3 lambda function resource ...
# resource "aws_lambda_function" "lambda3" {
#   function_name    = var.lambda3
#   role             = aws_iam_role.L3_lambda_role.arn
#   handler          = "load_handler3.lambda_handler"
#   runtime          = "python3.10"
#   s3_bucket        = aws_s3_bucket.code_bucket.id
#   s3_key           = "lambda3/lambda3.zip"
#   source_code_hash = data.archive_file.lambda3.output_base64sha256
#   architectures = ["arm64"]
#   timeout = 120 
#   memory_size = 256
#   layers = ["arn:aws:lambda:eu-west-2:336392948345:layer:AWSSDKPandas-Python310-Arm64:11", aws_lambda_layer_version.lambda3_layer_dependencies.arn] 
#   }

# # Creating the versioning for our L3 layer...
# resource "aws_lambda_layer_version" "lambda3_layer_dependencies" {
#   layer_name          = "lambda_layer3"
#   s3_bucket           = aws_s3_bucket.code_bucket.id
#   s3_key              = aws_s3_object.lambda3_layer_zip.key
#   compatible_runtimes = ["python3.10"]
#   source_code_hash    = base64sha256(filebase64("${path.module}/../aws_utils/layer_code3.zip"))
# }

# # Creating the permission that allows S3 to access the L3 function
# resource "aws_lambda_permission" "allow_s3_L3" {
#   action = "lambda:InvokeFunction"
#   function_name = aws_lambda_function.lambda3.function_name
#   principal = "s3.amazonaws.com"
#   source_arn = aws_s3_bucket.processed_bucket.arn
#   source_account = data.aws_caller_identity.current.account_id
# }
