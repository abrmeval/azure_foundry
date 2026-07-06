# ==============================================================================
# CONFIGURATION - Put your Azure Details Here
# ==============================================================================
$ClientId     = "your_client_id_here"
$TenantId     = "your_tenant_id_here"
$ClientSecret = "your_client_secret_here"
$FoundryEndpoint     = "https://your_azure_foundry_endpoint_here"

# ==============================================================================
# ACTION 1: ADD ENVIRONMENT VARIABLES
# ==============================================================================
function Set-AzureEnv {
    Write-Host "Setting Azure Environment Variables (Process Scope)..." -ForegroundColor Cyan
    
    [System.Environment]::SetEnvironmentVariable("AZURE_CLIENT_ID", $ClientId, "Process")
    [System.Environment]::SetEnvironmentVariable("AZURE_TENANT_ID", $TenantId, "Process")
    [System.Environment]::SetEnvironmentVariable("AZURE_CLIENT_SECRET", $ClientSecret, "Process")
    [System.Environment]::SetEnvironmentVariable("AZURE_FOUNDRY_ENDPOINT", $FoundryEndpoint, "Process")
    
    Write-Host "Variables successfully set! They will expire when this console closes." -ForegroundColor Green
}


# ==============================================================================
# ACTION 2: REMOVE ENVIRONMENT VARIABLES (Run this when finished)
# ==============================================================================
function Remove-AzureEnv {
    Write-Host "Removing Azure Environment Variables..." -ForegroundColor Yellow
    
    [System.Environment]::SetEnvironmentVariable("AZURE_CLIENT_ID", $null, "Process")
    [System.Environment]::SetEnvironmentVariable("AZURE_TENANT_ID", $null, "Process")
    [System.Environment]::SetEnvironmentVariable("AZURE_CLIENT_SECRET", $null, "Process")
    [System.Environment]::SetEnvironmentVariable("AZURE_FOUNDRY_ENDPOINT", $null, "Process")
    
    Write-Host "Variables successfully cleared from memory." -ForegroundColor Green
}


# ==============================================================================
# EXECUTION CONTROLLER
# ==============================================================================
# Uncomment the action you want to perform right now:

Set-AzureEnv
# Remove-AzureEnv
