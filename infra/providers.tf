provider "google" {
  project = "${local.project}-${var.environment}"
  region  = local.region
  zone    = local.zone
}
