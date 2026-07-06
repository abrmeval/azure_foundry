# Guidelines to set up your Azure environment for the Foundry project
- When working with Azure AI Projects SDK, you will need to set up your Azure environment with the necessary credentials and configurations. This guide will walk you through the steps to configure your Azure environment for the Foundry project.

## Step 1: Create an Azure Service Principal
## Step 2: Assign Roles to the Service Principal 
- Foundry Owner at the resource level (Foundry)
- Cognitive Services OpenAI Contributor at the resource level (Foundry)
# Step 3: Set Environment Variables
- Run the powershell script `Manage_AzureEnv.ps1` to set the environment variables for your Azure credentials. This script will configure the following environment variables:
  - `AZURE_CLIENT_ID`
  - `AZURE_TENANT_ID`
  - `AZURE_CLIENT_SECRET`

 # Step 4: Verify Environment Variables
- After running the script, you can verify that the environment variables have been set correctly by running
# Step 5: Run the application
- The applications will use DefaultAzureCredential to authenticate with Azure services. Ensure that the environment variables are set correctly before running the application. 