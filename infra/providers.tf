provider "google" {
  project = "${var.project}-${var.environment}"
  region  = var.region
  zone    = var.zone
}
