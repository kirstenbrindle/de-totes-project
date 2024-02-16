resource "aws_scheduler_schedule" "L1_scheduler" {
  name       = "L1_scheduler"
  flexible_time_window {
    mode = "OFF"
  }

  schedule_expression = "rate(5 minutes)"

  target {
    arn      = aws_lambda_function.lambda1.arn
    role_arn = aws_iam_role.L1_eventbridge_role.arn
  }
}


# module "eventbridge" {
#   source = "terraform-aws-modules/eventbridge/aws"
#   attach_lambda_policy = true
#   lambda_target_arns   = [lambda arn goes here]

#   schedules = {
#     lambda-cron = {
#       description         = "Trigger for a Lambda"
#       schedule_expression = "rate(5mins)"
#       timezone            = "Europe/London"
#       arn                 = [lambda arn goes here]
#       input               = jsonencode({ "job" : "cron-by-rate" })
#     }
#   }
# } 

# needs updating