terraform {
  backend "gcs" {
    bucket = "conversation-assistant-dev-bucket-tfstate"
    prefix = "terraform/state"
  }

  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "4.29.0"
    }
  }
}
