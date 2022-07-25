# Terraform state bucket
resource "google_storage_bucket" "default" {
  name          = "${var.project}-${var.environment}-bucket-tfstate"
  force_destroy = false
  location      = "US"
  storage_class = "STANDARD"
  versioning {
    enabled = true
  }
}
