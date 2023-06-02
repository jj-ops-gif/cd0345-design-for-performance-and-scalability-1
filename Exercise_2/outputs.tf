# TODO: Define the output variable for the lambda function.
output "lambda_id" {
  description = "ID of the lambda function"
  value       = aws_lambda_function.test_lambda.id
}