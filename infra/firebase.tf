resource "google_project" "default" {
  provider = google-beta

  project_id = "lachiejames-temp"
  name       = "lachiejames temp"
}

resource "google_firebase_project" "default" {
  provider = google-beta
  project  = google_project.default.project_id
}
