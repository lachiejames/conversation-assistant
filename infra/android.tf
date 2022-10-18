resource "google_storage_bucket" "bucket_android_assets" {
  name     = "${local.project}-${var.environment}-bucket-android-assets"
  location = "US"
}

resource "google_storage_bucket_iam_binding" "binding" {
  bucket  = google_storage_bucket.bucket_android_assets.name
  role    = "roles/storage.objectViewer"
  members = ["allUsers"]
}

# TODO: Figure out how to convert all of this to a for loop

resource "google_storage_bucket_object" "simple_gmail" {
  name   = "simple_gmail.gif"
  source = "../assets/generate_suggestions/simple_gmail.gif"
  bucket = google_storage_bucket.bucket_android_assets.name
}

resource "google_storage_bucket_object" "simple_messenger" {
  name   = "simple_messenger.gif"
  source = "../assets/generate_suggestions/simple_messenger.gif"
  bucket = google_storage_bucket.bucket_android_assets.name
}

resource "google_storage_bucket_object" "simple_outlook" {
  name   = "simple_outlook.gif"
  source = "../assets/generate_suggestions/simple_outlook.gif"
  bucket = google_storage_bucket.bucket_android_assets.name
}

resource "google_storage_bucket_object" "simple_slack" {
  name   = "simple_slack.gif"
  source = "../assets/generate_suggestions/simple_slack.gif"
  bucket = google_storage_bucket.bucket_android_assets.name
}

resource "google_storage_bucket_object" "simple_sms" {
  name   = "simple_sms.gif"
  source = "../assets/generate_suggestions/simple_sms.gif"
  bucket = google_storage_bucket.bucket_android_assets.name
}

resource "google_storage_bucket_object" "simple_whatsapp" {
  name   = "simple_whatsapp.gif"
  source = "../assets/generate_suggestions/simple_whatsapp.gif"
  bucket = google_storage_bucket.bucket_android_assets.name
}

resource "google_storage_bucket_object" "advanced_gmail" {
  name   = "advanced_gmail.gif"
  source = "../assets/generate_suggestions/advanced_gmail.gif"
  bucket = google_storage_bucket.bucket_android_assets.name
}

resource "google_storage_bucket_object" "advanced_messenger" {
  name   = "advanced_messenger.gif"
  source = "../assets/generate_suggestions/advanced_messenger.gif"
  bucket = google_storage_bucket.bucket_android_assets.name
}

resource "google_storage_bucket_object" "advanced_outlook" {
  name   = "advanced_outlook.gif"
  source = "../assets/generate_suggestions/advanced_outlook.gif"
  bucket = google_storage_bucket.bucket_android_assets.name
}

resource "google_storage_bucket_object" "advanced_slack" {
  name   = "advanced_slack.gif"
  source = "../assets/generate_suggestions/advanced_slack.gif"
  bucket = google_storage_bucket.bucket_android_assets.name
}

resource "google_storage_bucket_object" "advanced_sms" {
  name   = "advanced_sms.gif"
  source = "../assets/generate_suggestions/advanced_sms.gif"
  bucket = google_storage_bucket.bucket_android_assets.name
}

resource "google_storage_bucket_object" "advanced_whatsapp" {
  name   = "advanced_whatsapp.gif"
  source = "../assets/generate_suggestions/advanced_whatsapp.gif"
  bucket = google_storage_bucket.bucket_android_assets.name
}
