resource "google_storage_bucket" "bucket_firestore_backup" {
  name     = "${local.project}-${var.environment}-bucket-firestore-backup"
  location = "US"
}
