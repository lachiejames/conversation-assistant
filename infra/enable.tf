# Enable Cloud Functions API
resource "google_project_service" "cloudfunctions" {
  project = "${var.project}-${var.environment}"
  service = "cloudfunctions.googleapis.com"

  disable_dependent_services = true
  disable_on_destroy         = false
}

# Enable Cloud Build API
resource "google_project_service" "cloudbuild" {
  project = "${var.project}-${var.environment}"
  service = "cloudbuild.googleapis.com"

  disable_dependent_services = true
  disable_on_destroy         = false
}

# Enable Cloud Storage API
resource "google_project_service" "storage" {
  project = "${var.project}-${var.environment}"
  service = "storage.googleapis.com"

  disable_dependent_services = true
  disable_on_destroy         = false
}
