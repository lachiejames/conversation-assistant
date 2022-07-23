variable "environment" {
  type        = string
  description = "'dev' or 'prod'"
  default     = "prod"
}

variable "region" {
  type        = string
  description = "GCP default region"
  default     = "us-west1"
}

variable "project" {
  type        = string
  description = "Application Name"
  default     = "conversation-assistant"
}
