terraform {
  backend "gcs" {
    bucket = "${var.project}-${var.environment}-bucket-tfstate"
    prefix = "terraform/state"
  }

  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "4.29.0"
    }
  }
}
