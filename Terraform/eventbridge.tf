# module "eventbridge" {
#   source = "terraform-aws-modules/eventbridge/aws"
#   attach_lambda_policy = true
#   lambda_target_arns   = [lambda arn goes here]

#   schedules = {
#     lambda-cron = {
#       description         = "Trigger for a Lambda"
#       schedule_expression = "cron(*/5 * * * ? *)"
#       timezone            = "Europe/London"
#       arn                 = [lambda arn goes here]
#       input               = jsonencode({ "job" : "cron-by-rate" })
#     }
#   }
# } 