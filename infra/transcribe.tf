resource "google_storage_bucket" "bucket-stt-workspace" {
  name     = "${local.project}-${var.environment}-bucket-stt-workspace"
  location = "US"
}
