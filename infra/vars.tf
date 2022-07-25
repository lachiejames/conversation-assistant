variable "project" {
  type        = string
  description = "Application Name"
  default     = "conversation-assistant"
}

variable "environment" {
  type        = string
  description = "'dev' or 'prod'"
  default     = "dev"
}

variable "region" {
  type        = string
  description = "GCP default region"
  default     = "us-west1"
}

variable "zone" {
  type        = string
  description = "GCP default zone"
  default     = "us-west1-a"
}

variable "function_name" {
  type        = string
  description = "GCP default zone"
  default     = "generate-suggestions"
}
