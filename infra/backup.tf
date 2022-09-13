resource "google_storage_bucket" "bucket-firestore-backup" {
  name     = "${local.project}-${var.environment}-bucket-firestore-backup"
  location = "US"
}
