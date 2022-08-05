terraform {
  # NOTE: You will need to comment this out the first time you run `terraform init` on a new project so 
  # that the TF state bucket is created first
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
