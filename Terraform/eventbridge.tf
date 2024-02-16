# module "eventbridge" {
#   source = "terraform-aws-modules/eventbridge/aws"
#   attach_lambda_policy = true
#   lambda_target_arns   = aws_lambda_function.L1_injestion.arn

#   schedules = {
#     lambda-cron = {
#       description         = "Trigger for a Lambda"
#       schedule_expression = "cron(*/5 * * * ? *)"
#       timezone            = "Europe/London"
#       arn                 = aws_lambda_function.L1_injestion.arn
#       input               = jsonencode({ "job" : "cron-by-rate" })
#     }
#   }
# } 