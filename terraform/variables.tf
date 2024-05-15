variable "region" {
  type    = string
  default = "eu-west-2"
}

variable "service_name" {
  type    = string
  default = "m8-stock-checker"
}

variable "runtime" {
  type    = string
  default = "python3.9"
}

variable "handler" {
  type    = string
  default = "main.lambda_handler"
}

variable "timeout" {
  type    = number
  default = 900
}

variable "memory_size" {
  type    = number
  default = 128
}

variable "lambda_role_name" {
  type    = string
  default = "lambda-exec-role"
}

variable "lambda_policy_name" {
  type    = string
  default = "lambda-exec-policy"
}

variable "user_key" {
  type = string
}

variable "api_token" {
  type = string
}
