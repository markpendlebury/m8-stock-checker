resource "aws_lambda_function" "lambda" {
  function_name    = "${var.service_name}-lambda"
  image_uri        = "${data.aws_ecr_repository.ecr.repository_url}:latest"
  package_type     = "Image"
  timeout          = var.timeout
  memory_size      = var.memory_size
  source_code_hash = null
  role             = aws_iam_role.lambda_exec.arn


  environment {
    variables = {
      user_key  = var.user_key,
      api_token = var.api_token
    }
  }

  depends_on = [
    aws_ecr_repository.ecr
  ]
}

