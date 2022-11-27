resource "aws_iam_user" "user" {
  for_each = toset(var.user_name)
  name        = each.value
}