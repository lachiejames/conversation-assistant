terraform {
 backend "gcs" {
   bucket  = "conversation-assistant-prod-bucket-tfstate"
   prefix  = "terraform/state"
 }
}
