variable "environment" {
  type        = string
  description = "'dev' or 'prod'"
  default     = "dev"
}

variable "function_name" {
  type        = string
  description = "GCP default zone"
  default     = "generate-suggestions"
}
