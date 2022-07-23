# Enable Cloud Functions API
resource "google_project_service" "cloudfunctions" {
  project = var.project
  service = "cloudfunctions.googleapis.com"

  disable_dependent_services = true
  disable_on_destroy         = false
}

# Enable Cloud Build API
resource "google_project_service" "cloudbuild" {
  project = var.project
  service = "cloudbuild.googleapis.com"

  disable_dependent_services = true
  disable_on_destroy         = false
}

# Enable Cloud Storage API
resource "google_project_service" "storage" {
  project = var.project
  service = "storage.googleapis.com"

  disable_dependent_services = true
  disable_on_destroy         = false
}
