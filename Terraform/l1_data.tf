data "aws_caller_identity" "current" {}

data "aws_region" "current" {}

data "archive_file" "lambda1" {
  type        = "zip"
  source_dir = "${path.module}/../src/extract_handler1"
  output_path = "${path.module}/../lambda1.zip"
}

data "archive_file" "layer_code1" {
  type        = "zip"
  source_dir = "${path.module}/../aws_utils/layer_code1"
  output_path = "${path.module}/../aws_utils/layer_code1.zip"
}
