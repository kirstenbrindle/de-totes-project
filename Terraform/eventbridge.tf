resource "aws_scheduler_schedule" "L1_scheduler" {
  name = "L1_scheduler"
  flexible_time_window {
    mode = "OFF"
  }

  schedule_expression = "rate(5 minutes)"

  target {
    arn      = aws_lambda_function.lambda1.arn
    role_arn = aws_iam_role.L1_eventbridge_role.arn
  }
}

