resource "google_storage_bucket" "bucket_android_assets" {
  name     = "${local.project}-${var.environment}-bucket-android-assets"
  location = "US"
}

resource "google_storage_bucket_iam_binding" "binding" {
  bucket  = google_storage_bucket.bucket_android_assets.name
  role    = "roles/storage.objectViewer"
  members = ["allUsers"]
}

resource "google_storage_bucket_object" "android_assets" {
  for_each = fileset("../assets/generate_suggestions/", "*.gif")

  name         = each.value
  content_type = "image/gif"
  source       = "${path.module}/../assets/generate_suggestions/${each.key}"
  bucket       = google_storage_bucket.bucket_android_assets.name
}