data "archive_file" "lambda3" {
  type        = "zip"
  source_dir = "${path.module}/../src/load_handler3"
  output_path = "${path.module}/../lambda3.zip"
}

data "archive_file" "layer_code3" {
  type        = "zip"
  source_dir = "${path.module}/../aws_utils/layer_code3"
  output_path = "${path.module}/../aws_utils/layer_code3.zip"
}