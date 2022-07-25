terraform {
  backend "gcs" {
    bucket = "conversation-assistant-prod-bucket-tfstate"
    prefix = "terraform/state"
  }

  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "4.29.0"
    }
  }
}
