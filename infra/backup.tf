resource "google_storage_bucket" "bucket" {
  name     = "${local.project}-${var.environment}-bucket-firestore-backup"
  location = "US"
}
