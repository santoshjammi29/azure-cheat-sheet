# 💻 Azure CLI (`az`) Production Cheat Sheet

A battle-tested reference guide containing essential **Azure CLI (`az`)** commands for Cloud Architects, DevOps Engineers, and Data Platform Engineers.

---

## 📑 Table of Contents
1. [CLI Setup, Context & Output Formatting](#1-cli-setup-context--output-formatting)
2. [Resource Groups & Tags](#2-resource-groups--tags)
3. [Identity, Entra ID & RBAC](#3-identity-entra-id--rbac)
4. [Storage Accounts & ADLS Gen2](#4-storage-accounts--adls-gen2)
5. [Compute, Virtual Machines & VMSS](#5-compute-virtual-machines--vmss)
6. [Containers: AKS & Container Apps (ACA)](#6-containers-aks--container-apps-aca)
7. [App Service & Azure Functions](#7-app-service--azure-functions)
8. [Databases: Cosmos DB, Azure SQL, PostgreSQL](#8-databases-cosmos-db-azure-sql-postgresql)
9. [Analytics: Microsoft Fabric, Synapse & Databricks](#9-analytics-microsoft-fabric-synapse--databricks)
10. [AI Services & Azure OpenAI](#10-ai-services--azure-openai)
11. [Networking, Private Endpoints & DNS](#11-networking-private-endpoints--dns)
12. [Security & Azure Key Vault](#12-security--azure-key-vault)
13. [Monitoring, Log Analytics & Diagnostics](#13-monitoring-log-analytics--diagnostics)
14. [FinOps & Resource Cleanup Scripts](#14-finops--resource-cleanup-scripts)

---

## 1. CLI Setup, Context & Output Formatting

### Authentication & Account Selection
```bash
# Interactive web login
az login

# Device-code login (for headless Linux / dev containers)
az login --use-device-code

# Login using Managed Identity (inside Azure VM / Container)
az login --identity

# Login using Service Principal (CI/CD)
az login --service-principal \
  --username "$AZURE_CLIENT_ID" \
  --password "$AZURE_CLIENT_SECRET" \
  --tenant "$AZURE_TENANT_ID"

# List all subscriptions accessible to current identity
az account list --output table

# Set active subscription by Name or ID
az account set --subscription "Production-DataPlatform-Sub"
az account set --subscription "00000000-0000-0000-0000-000000000000"

# Verify currently active subscription and tenant
az account show --output json
```

### JMESPath Filtering (`--query`) & Formatting
```bash
# Output formats: table, json, jsonc, tsv, yaml
az group list --output table

# Filter resources by property (e.g. running VMs in eastus)
az vm list --query "[?location=='eastus' && powerState=='VM running'].{Name:name, RG:resourceGroup, Size:hardwareProfile.vmSize}" --output table

# Extract a single string value cleanly for Bash assignment (TSV eliminates quotes)
VNET_ID=$(az network vnet show -g rg-core-prod -n vnet-core --query id -o tsv)

# Top 5 most expensive disks by size
az disk list --query "reverse(sort_by([].{name:name, sizeGb:diskSizeGb, tier:sku.name}, &sizeGb))[0:5]" -o table
```

---

## 2. Resource Groups & Tags

```bash
# Create a resource group with mandatory governance tags
az group create \
  --name rg-analytics-prod-eastus \
  --location eastus \
  --tags Environment=Production CostCenter=FinAnalytics Owner=DataEng

# Apply or merge tags without overwriting existing ones
az tag update \
  --resource-id "/subscriptions/$SUB_ID/resourceGroups/rg-analytics-prod-eastus" \
  --operation Merge \
  --tags Compliance=SOX Project=OneLake

# List all resources in a resource group
az resource list --resource-group rg-analytics-prod-eastus -o table

# Delete resource group asynchronously (non-blocking in terminal)
az group delete --name rg-analytics-dev --no-wait --yes
```

---

## 3. Identity, Entra ID & RBAC

### Managed Identities
```bash
# Create a User-Assigned Managed Identity (UAMI)
az identity create \
  --name id-datalake-ingest \
  --resource-group rg-security-prod \
  --location eastus

# Get Principal ID and Client ID of the Managed Identity
UAMI_PRINCIPAL_ID=$(az identity show -g rg-security-prod -n id-datalake-ingest --query principalId -o tsv)
UAMI_CLIENT_ID=$(az identity show -g rg-security-prod -n id-datalake-ingest --query clientId -o tsv)
```

### Role-Based Access Control (RBAC)
```bash
# Assign 'Storage Blob Data Contributor' to a Managed Identity scoped to a specific Storage Account
az role assignment create \
  --assignee "$UAMI_PRINCIPAL_ID" \
  --role "Storage Blob Data Contributor" \
  --scope "/subscriptions/$SUB_ID/resourceGroups/rg-data-prod/providers/Microsoft.Storage/storageAccounts/stlakehouseprod"

# Assign 'Key Vault Secrets User' scoped to a specific Key Vault
az role assignment create \
  --assignee "$UAMI_PRINCIPAL_ID" \
  --role "Key Vault Secrets User" \
  --scope "/subscriptions/$SUB_ID/resourceGroups/rg-sec-prod/providers/Microsoft.KeyVault/vaults/kv-data-prod"

# List role assignments for a user or principal
az role assignment list --assignee "developer@company.com" --output table

# Verify effective permissions on a resource
az role assignment list --scope "/subscriptions/$SUB_ID/resourceGroups/rg-data-prod" --output table
```

---

## 4. Storage Accounts & ADLS Gen2

```bash
# Create an ADLS Gen2 Storage Account (Hierarchical Namespace enabled)
az storage account create \
  --name stlakehouseprod01 \
  --resource-group rg-data-prod \
  --location eastus \
  --sku Standard_ZRS \
  --kind StorageV2 \
  --enable-hierarchical-namespace true \
  --min-tls-version TLS1_2 \
  --allow-blob-public-access false \
  --require-infrastructure-encryption true

# Create filesystem / container using Entra ID authentication (no keys required)
az storage container create \
  --account-name stlakehouseprod01 \
  --name bronze \
  --auth-mode login

az storage container create \
  --account-name stlakehouseprod01 \
  --name silver \
  --auth-mode login

az storage container create \
  --account-name stlakehouseprod01 \
  --name gold \
  --auth-mode login

# Upload data recursively into ADLS Gen2 using Entra ID auth
az storage blob upload-batch \
  --destination bronze \
  --source ./telemetry_dump/ \
  --account-name stlakehouseprod01 \
  --destination-path "raw/telemetry/2026/01/" \
  --auth-mode login

# Change blob tier to Archive or Cool
az storage blob tier set \
  --account-name stlakehouseprod01 \
  --container-name bronze \
  --name "raw/archive_2025.tar.gz" \
  --tier Archive \
  --auth-mode login
```

---

## 5. Compute, Virtual Machines & VMSS

```bash
# Create an Ubuntu 24.04 LTS VM with SSH Key and accelerated networking
az vm create \
  --resource-group rg-compute-prod \
  --name vm-worker-01 \
  --image Ubuntu2404 \
  --size Standard_D4as_v5 \
  --admin-username azureuser \
  --generate-ssh-keys \
  --vnet-name vnet-core \
  --subnet snet-workers \
  --public-ip-address "" \
  --storage-sku Premium_LRS

# Deallocate VM to stop compute charges (finops imperative: stopped != deallocated!)
az vm deallocate --resource-group rg-compute-prod --name vm-worker-01

# Start deallocated VM
az vm start --resource-group rg-compute-prod --name vm-worker-01

# Run an ad-hoc bash script inside an Azure Linux VM without SSH opening
az vm run-command invoke \
  --resource-group rg-compute-prod \
  --name vm-worker-01 \
  --command-id RunShellScript \
  --scripts "df -h && docker ps -a"

# List VM sizes available in a region with vCPU and RAM details
az vm list-sizes --location eastus --query "[?contains(name, 'Standard_D4')].{Name:name, vCPUs:numberOfCores, RAM_GB:memoryInMB/1024}" -o table
```

---

## 6. Containers: AKS & Container Apps (ACA)

### Azure Kubernetes Service (AKS)
```bash
# Create a production-ready AKS cluster with Azure CNI Overlay, System Assigned Identity & Azure RBAC
az aks create \
  --resource-group rg-k8s-prod \
  --name aks-core-prod \
  --node-count 3 \
  --node-vm-size Standard_D8ds_v5 \
  --network-plugin azure \
  --network-plugin-mode overlay \
  --enable-managed-identity \
  --enable-azure-rbac \
  --enable-cluster-autoscaler \
  --min-count 3 \
  --max-count 10 \
  --generate-ssh-keys

# Download kubeconfig credentials to ~/.kube/config
az aks get-credentials --resource-group rg-k8s-prod --name aks-core-prod --overwrite-existing

# Add a dedicated GPU node pool for AI inference
az aks nodepool add \
  --resource-group rg-k8s-prod \
  --cluster-name aks-core-prod \
  --name gpunodes \
  --node-count 1 \
  --node-vm-size Standard_NC6s_v3 \
  --node-taints sku=gpu:NoSchedule

# Upgrade AKS cluster kubernetes version
az aks upgrade \
  --resource-group rg-k8s-prod \
  --name aks-core-prod \
  --kubernetes-version 1.30.2 \
  --yes
```

### Azure Container Apps (ACA)
```bash
# Create ACA Environment (with Log Analytics integration)
az containerapp env create \
  --name aca-env-prod \
  --resource-group rg-apps-prod \
  --location eastus

# Deploy a Serverless Container App scaling to zero with KEDA HTTP scaling
az containerapp create \
  --name api-order-service \
  --resource-group rg-apps-prod \
  --environment aca-env-prod \
  --image myregistry.azurecr.io/orders:v2.1 \
  --target-port 8080 \
  --ingress external \
  --min-replicas 0 \
  --max-replicas 20 \
  --scale-rule-name http-rule \
  --scale-rule-type http \
  --scale-rule-http-concurrency 100
```

---

## 7. App Service & Azure Functions

```bash
# Deploy a code directory directly to App Service via ZIP deploy
az webapp deploy \
  --resource-group rg-web-prod \
  --name app-customer-portal \
  --src-path ./dist.zip \
  --type zip

# Tail real-time live application logs from web app
az webapp log tail --resource-group rg-web-prod --name app-customer-portal

# Set environment variables / application settings securely
az webapp config appsettings set \
  --resource-group rg-web-prod \
  --name app-customer-portal \
  --settings \
    NODE_ENV=production \
    KEY_VAULT_URI=https://kv-data-prod.vault.azure.net/

# Create a Flex Consumption Azure Function App (scale-to-zero, low cold start)
az functionapp create \
  --resource-group rg-func-prod \
  --name fn-event-processor \
  --storage-account stfnstoreprod \
  --flexconsumption-location eastus \
  --runtime python \
  --runtime-version 3.11
```

---

## 8. Databases: Cosmos DB, Azure SQL, PostgreSQL

### Azure Cosmos DB (NoSQL API with Vector Search)
```bash
# Create Cosmos DB account with Autoscale RU/s enabled
az cosmosdb create \
  --name cosmos-enterprise-prod \
  --resource-group rg-db-prod \
  --default-consistency-level Session \
  --locations regionName=eastus failoverPriority=0 isZoneRedundant=true

# Create Database
az cosmosdb sql database create \
  --account-name cosmos-enterprise-prod \
  --resource-group rg-db-prod \
  --name CustomerDB

# Create Container with partition key and autoscale throughput (Max 4,000 RU/s)
az cosmosdb sql container create \
  --account-name cosmos-enterprise-prod \
  --resource-group rg-db-prod \
  --database-name CustomerDB \
  --name Orders \
  --partition-key-path "/tenant_id" \
  --max-throughput 4000
```

### PostgreSQL Flexible Server (with `pgvector` ready)
```bash
# Provision PostgreSQL Flexible Server with High Availability
az postgres flexible-server create \
  --resource-group rg-db-prod \
  --name pg-flex-prod-01 \
  --location eastus \
  --admin-user psqladmin \
  --sku-name Standard_D4ds_v5 \
  --tier GeneralPurpose \
  --storage-size 128 \
  --version 16 \
  --high-availability ZoneRedundant
```

---

## 9. Analytics: Microsoft Fabric, Synapse & Databricks

### Microsoft Fabric Capacity
```bash
# Provision Fabric F64 capacity
az fabric capacity create \
  --resource-group rg-fabric-prod \
  --capacity-name capfabricprod01 \
  --location eastus \
  --sku F64 \
  --administration-members "santosh@company.com"

# FinOps: Suspend (Pause) Fabric Capacity outside business hours
az fabric capacity suspend \
  --resource-group rg-fabric-prod \
  --capacity-name capfabricprod01

# FinOps: Resume Fabric Capacity
az fabric capacity resume \
  --resource-group rg-fabric-prod \
  --capacity-name capfabricprod01
```

### Azure Synapse & Azure Databricks
```bash
# Pause a Synapse Dedicated SQL Pool
az synapse sql pool pause \
  --workspace-name syn-workspace-prod \
  --name DedicatedPool01 \
  --resource-group rg-synapse-prod

# Resume a Synapse Dedicated SQL Pool
az synapse sql pool resume \
  --workspace-name syn-workspace-prod \
  --name DedicatedPool01 \
  --resource-group rg-synapse-prod

# Create an Azure Databricks Premium Workspace (Unity Catalog enabled)
az databricks workspace create \
  --resource-group rg-databricks-prod \
  --name adb-lakehouse-prod \
  --location eastus \
  --sku premium
```

---

## 10. AI Services & Azure OpenAI

```bash
# Create an Azure OpenAI multi-service cognitive account
az cognitiveservices account create \
  --name oai-enterprise-prod \
  --resource-group rg-ai-prod \
  --location eastus \
  --kind OpenAI \
  --sku S0 \
  --custom-domain oai-enterprise-prod

# Deploy GPT-4o model
az cognitiveservices account deployment create \
  --resource-group rg-ai-prod \
  --name oai-enterprise-prod \
  --deployment-name gpt-4o \
  --model-name gpt-4o \
  --model-version "2024-08-06" \
  --model-format OpenAI \
  --sku-capacity 50 \
  --sku-name Standard

# Deploy text-embedding-3-large embedding model
az cognitiveservices account deployment create \
  --resource-group rg-ai-prod \
  --name oai-enterprise-prod \
  --deployment-name text-embedding-3-large \
  --model-name text-embedding-3-large \
  --model-version "1" \
  --model-format OpenAI \
  --sku-capacity 50 \
  --sku-name Standard

# Provision Azure AI Search (Semantic Ranker & Vector Search)
az search service create \
  --name search-legal-docs-prod \
  --resource-group rg-ai-prod \
  --sku Standard \
  --partition-count 1 \
  --replica-count 2
```

---

## 11. Networking, Private Endpoints & DNS

```bash
# Create Hub VNet and Spoke VNet
az network vnet create -g rg-net-prod -n vnet-hub --address-prefix 10.0.0.0/16 -l eastus
az network vnet create -g rg-net-prod -n vnet-spoke-data --address-prefix 10.1.0.0/16 -l eastus

# Peer Hub and Spoke VNets
az network vnet peering create -g rg-net-prod -n HubToData --vnet-name vnet-hub --remote-vnet vnet-spoke-data --allow-vnet-access
az network vnet peering create -g rg-net-prod -n DataToHub --vnet-name vnet-spoke-data --remote-vnet vnet-hub --allow-vnet-access

# Create a Private Endpoint for Storage Blob into Subnet
STORAGE_ID=$(az storage account show -g rg-data-prod -n stlakehouseprod01 --query id -o tsv)
SUBNET_ID=$(az network vnet subnet show -g rg-net-prod --vnet-name vnet-spoke-data --name snet-private-endpoints --query id -o tsv)

az network private-endpoint create \
  --resource-group rg-net-prod \
  --name pe-stlakehouse-blob \
  --vnet-name vnet-spoke-data \
  --subnet "$SUBNET_ID" \
  --private-connection-resource-id "$STORAGE_ID" \
  --group-id blob \
  --connection-name conn-stlakehouse-blob

# Link Private DNS Zone to VNet
az network private-dns zone create -g rg-net-prod -n privatelink.blob.core.windows.net
az network private-dns link vnet create \
  -g rg-net-prod \
  -z privatelink.blob.core.windows.net \
  -n link-hub \
  -v vnet-hub \
  -e false
```

---

## 12. Security & Azure Key Vault

```bash
# Create Key Vault enforcing Azure RBAC authorization (no legacy access policies)
az keyvault create \
  --name kv-security-prod01 \
  --resource-group rg-sec-prod \
  --location eastus \
  --enable-rbac-authorization true \
  --enable-soft-delete true \
  --retention-days 90 \
  --enable-purge-protection true

# Add a Secret to Key Vault
az keyvault secret set \
  --vault-name kv-security-prod01 \
  --name "DatabricksToken" \
  --value "dapi0123456789abcdef"

# Read a Secret value using CLI
az keyvault secret show \
  --vault-name kv-security-prod01 \
  --name "DatabricksToken" \
  --query value -o tsv
```

---

## 13. Monitoring, Log Analytics & Diagnostics

```bash
# Create Log Analytics Workspace
az monitor log-analytics workspace create \
  --resource-group rg-ops-prod \
  --workspace-name law-core-prod \
  --location eastus \
  --retention-time 90

LAW_ID=$(az monitor log-analytics workspace show -g rg-ops-prod -n law-core-prod --query id -o tsv)

# Stream diagnostic logs from Key Vault to Log Analytics
az monitor diagnostic-settings create \
  --name "diag-to-law" \
  --resource "/subscriptions/$SUB_ID/resourceGroups/rg-sec-prod/providers/Microsoft.KeyVault/vaults/kv-security-prod01" \
  --workspace "$LAW_ID" \
  --logs '[{"categoryGroup": "allLogs", "enabled": true}]' \
  --metrics '[{"category": "AllMetrics", "enabled": true}]'
```

---

## 14. FinOps & Resource Cleanup Scripts

### Find Unattached Managed Disks (Burning Money Idle)
```bash
az disk list \
  --query "[?managedBy==null].{Name:name, ResourceGroup:resourceGroup, DiskSizeGB:diskSizeGb, Tier:sku.name}" \
  --output table
```

### Find Unassociated Public IP Addresses
```bash
az network public-ip list \
  --query "[?ipConfiguration==null].{Name:name, ResourceGroup:resourceGroup, Address:ipAddress}" \
  --output table
```

### Export Cost Analysis for Current Month Grouped by Service
```bash
az consumption usage list \
  --start-date "$(date +%Y-%m-01)" \
  --end-date "$(date +%Y-%m-%d)" \
  --query "[].{Meter:meterDetails.meterName, Category:meterDetails.meterCategory, PreTaxCost:pretaxCost}" \
  --output table
```

---

[← Back to Main Cheat Sheet](../README.md)
