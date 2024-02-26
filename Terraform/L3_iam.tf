# creating secretsmanager policy doc...
data "aws_iam_policy_document" "wh_access_doc" {
  statement {
    effect = "Allow"

  principals {
      type        = "AWS"
      identifiers = ["LAMBDA3 ARN"]
    }

    actions   = ["secretsmanager:GetSecretValue"]
    resources = ["arn:aws:secretsmanager:eu-west-2:533267264466:secret:warehouseCredentials-ZMya4g"]
  }
}

#creating secretmanager policy...
resource "aws_secretsmanager_secret_policy" "wh_access_policy" {
  secret_arn = "arn:aws:secretsmanager:eu-west-2:533267264466:secret:warehouseCredentials-ZMya4g"
  policy     = data.aws_iam_policy_document.wh_access_doc.json
}

# # Attaching SecretManager Policy to L3 IAM Role ...
# resource "aws_iam_role_policy_attachment" "wh_access_policy_attachment" {
#   role       = aws_iam_role.L3_lambda_role.name
#   policy_arn = aws_secretsmanager_secret_policy.wh_access_policy.arn
# }