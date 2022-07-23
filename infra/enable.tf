# Enable Cloud Functions API
resource "google_project_service" "cloudfunctions" {
  project = "${var.project}-${var.environment}"
  service = "cloudfunctions.googleapis.com"
}

# Enable Cloud Build API
resource "google_project_service" "cloudbuild" {
  project = "${var.project}-${var.environment}"
  service = "cloudbuild.googleapis.com"
}

# Enable Cloud Storage API
resource "google_project_service" "storage" {
  project = "${var.project}-${var.environment}"
  service = "storage.googleapis.com"
}
