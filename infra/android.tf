# Stores resources for the Conversation Assistant Android app
resource "google_storage_bucket" "bucket-android-assets" {
  name     = "${local.project}-${var.environment}-bucket-android-assets"
  location = "US"
}
