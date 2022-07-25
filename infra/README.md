# infra

Before this can be deployed, you must do the following:

1. Create a GCP project

2. Create a Service Account and download the credentials

3. Add permissions to your Service accounts until it looks like this:

![GCP Service Accounts](../.github/assets/gcp-service-account.png)

3. Enable the following APIs

   - Secret Manager API
   - Cloud Build API
   - Compute Engine API
   - Cloud Translation API
   - Cloud Functions API

4. Add the following secrets to Secret Manager

   - OPENAI_API_KEY
