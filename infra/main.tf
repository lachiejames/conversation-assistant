terraform {
  required_providers {
    google = {
      source = "hashicorp/google"
      version = "4.29.0"
    }
  }
}

provider "google" {
  credentials = file("../google-application-credentials.json")

  project = "conversation-assistant-prod"
  region  = "us-central1"
  zone    = "us-central1-c"
}

resource "google_compute_network" "vpc_network" {
  name = "terraform-network"
}
