locals {
  apps      = ["Gmail", "Messenger", "Outlook", "Slack", "SMS", "WhatsApp"]
  tutorials = ["Simple", "Advanced"]
}

resource "google_storage_bucket" "bucket_android_assets" {
  name     = "${local.project}-${var.environment}-bucket-android-assets"
  location = "US"
}

resource "google_storage_default_object_access_control" "public" {
  bucket = google_storage_bucket.bucket_android_assets.name
  role   = "READER"
  entity = "allUsers"
}

# TODO: Figure out how to convert all of this to a for loop
resource "google_storage_bucket_object" "android_assets" {
  for_each = {
    for tutorial in local.tutorials : "${tutorials}-android-assets" => {
      for app in local.apps : "${app}-android" => {
        bucket = google_storage_bucket.bucket_android_assets.name
        name   = "${tutorial}_${app}.gif"
        source = "../assets/generate_suggestions/${tutorial}_${app}.gif"
      }
    }
  }

  bucket = each.value.bucket
  name   = each.value.name
  source = each.value.source
}
