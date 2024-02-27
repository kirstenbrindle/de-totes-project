resource "aws_cloudwatch_log_metric_filter" "error_log2" {
  name           = "TotesErrorL2"
  pattern        = "ERROR"
  log_group_name = "/aws/lambda/${var.lambda2}"

  metric_transformation {
    name      = "ErrorCount"
    namespace = "lambda2_error"
    value     = "1"
  }
}

resource "aws_cloudwatch_metric_alarm" "alert_errors_L2" {
  alarm_name          = "ErrorAlarmL2"
  comparison_operator = "GreaterThanOrEqualToThreshold"
  evaluation_periods  = 1
  metric_name         = aws_cloudwatch_log_metric_filter.error_log2.metric_transformation[0].name
  namespace           = aws_cloudwatch_log_metric_filter.error_log2.metric_transformation[0].namespace
  period              = 60
  statistic           = "Sum"
  alarm_description   = "This metric monitors error instances for L2: transform_handler2"
  actions_enabled     = "true"
  alarm_actions       = ["arn:aws:sns:eu-west-2:533267264466:bitme-error-alerts"]
  threshold           = 1
}
