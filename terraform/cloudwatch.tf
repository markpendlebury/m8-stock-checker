resource "aws_cloudwatch_log_group" "lambda" {
  name              = "/aws/lambda/${aws_lambda_function.lambda.function_name}"
  retention_in_days = 30
}

resource "aws_cloudwatch_event_rule" "once_per_hour" {
  name                = "once_per_hour"
  description         = "Run once per hour"
  schedule_expression = "cron(0 * * * ? *)"
}

resource "aws_cloudwatch_event_target" "run_lambda_once_a_day" {
  rule = aws_cloudwatch_event_rule.once_per_hour.name
  arn  = aws_lambda_function.lambda.arn
}

resource "aws_lambda_permission" "allow_cloudwatch_to_call_lambda" {
  statement_id  = "AllowExecutionFromCloudWatch"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.lambda.function_name
  principal     = "events.amazonaws.com"
  source_arn    = aws_cloudwatch_event_rule.once_per_hour.arn
}
