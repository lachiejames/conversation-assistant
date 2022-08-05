# infra

Before this can be deployed, you must do the following:

1. Create a GCP project

2. Create a Service Account and download the credentials as per [these steps](https://learn.hashicorp.com/tutorials/terraform/google-cloud-platform-build?in=terraform/gcp-get-started)

3. Enable the following APIs

   - Cloud Build API
   - Cloud Functions API
   - Cloud Storage API
   - Cloud Translation API
   - Compute Engine API
   - Secret Manager API

4. Add permissions to your Service accounts until it looks like this:

![GCP Service Accounts](../.github/assets/gcp-service-account.png)

5. Add the following secrets to Secret Manager

   - OPENAI_API_KEY

6. Create a [Cloud Storage bucket](https://cloud.google.com/docs/terraform/resource-management/store-state) to store Terraform state

7. In your terminal, sign into your GCP account using the service account credentials

```
gcloud auth activate-service-account deploy@conversation-assistant-dev.iam.gserviceaccount.com --key-file=/Users/lachiejames/dev/conversation-assistant/gcp-credentials-dev.json     
```

8. To deploy infra

```
cd infra
terraform init -backend-config="environment=dev"
terraform deploy -var="environment=dev"
```
