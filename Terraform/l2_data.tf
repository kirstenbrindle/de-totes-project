data "archive_file" "lambda2" {
  type        = "zip"
  source_dir  = "${path.module}/../src/transform_handler2"
  output_path = "${path.module}/../lambda2.zip"
}

data "archive_file" "layer_code2" {
  type        = "zip"
  source_dir  = "${path.module}/../aws_utils/layer_code2"
  output_path = "${path.module}/../aws_utils/layer_code2.zip"
}
