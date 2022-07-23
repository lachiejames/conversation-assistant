terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "4.29.0"
    }
  }
}

provider "google" {
  credentials = file("../google-application-credentials.json")

  project = "${var.project}-${var.environment}"
  region  = "us-central1"
  zone    = "us-central1-c"
}

resource "google_storage_bucket" "default" {
  name          = "${var.project}-${var.environment}-bucket-tfstate"
  force_destroy = false
  location      = "US"
  storage_class = "STANDARD"
  versioning {
    enabled = true
  }
}