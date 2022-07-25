data "google_secret_manager_secret_version" "OPENAI_API_KEY" {
  secret = "OPENAI_API_KEY"
}
