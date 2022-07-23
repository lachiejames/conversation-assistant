resource "google_storage_bucket" "bucket" {
  name     = "${var.project}-${var.environment}-bucket-${var.function_name}"
  location = "US"
}

data "archive_file" "archive" {
  type        = "zip"
  source  = "../"
  output_path = "/tmp/function.zip"
}

resource "google_storage_bucket_object" "object" {
  name         = "${var.function_name}.zip"
  content_type = "application/zip"
  source       = data.archive_file.archive.output_path
  bucket       = google_storage_bucket.bucket.name
}

resource "google_cloudfunctions_function" "function" {
  name        = "${var.function_name}-function"
  description = "Generates message suggestions for a user to respond with based upon their conversation history, and some context parameters"
  runtime     = "python39"

  available_memory_mb          = 512
  source_archive_bucket        = google_storage_bucket.bucket.name
  source_archive_object        = google_storage_bucket_object.object.name
  trigger_http                 = true
  https_trigger_security_level = "SECURE_ALWAYS"
  timeout                      = 60
  entry_point                  = "generate_suggestions"
}
