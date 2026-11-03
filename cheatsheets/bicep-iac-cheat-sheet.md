# 🏗️ Azure Bicep & IaC Developer Cheat Sheet

A comprehensive reference for deploying declarative Azure infrastructure using **Azure Bicep** and the **Azure Developer CLI (`azd`)**.

---

## 📑 Table of Contents
1. [Why Bicep?](#1-why-bicep)
2. [CLI Workflow & Commands](#2-cli-workflow--commands)
3. [Syntax Fundamentals & Decorators](#3-syntax-fundamentals--decorators)
4. [Parameters, Variables & Outputs](#4-parameters-variables--outputs)
5. [Modules & Composition](#5-modules--composition)
6. [Loops & Conditionals](#6-loops--conditionals)
7. [Referencing Existing Resources](#7-referencing-existing-resources)
8. [Secrets & Key Vault Integration](#8-secrets--key-vault-integration)
9. [RBAC Role Assignments in Bicep](#9-rbac-role-assignments-in-bicep)
10. [Production Example: Storage + Private Endpoint + Key Vault](#10-production-example-storage--private-endpoint--key-vault)
11. [Azure Developer CLI (`azd`) Fast Track](#11-azure-developer-cli-azd-fast-track)

---

## 1. Why Bicep?

Bicep is Microsoft's domain-specific language (DSL) for provisioning Azure resources declaratively.
- **Zero State File Management**: Unlike Terraform, Bicep requires no remote state backend or state locking. The Azure Resource Manager (ARM) engine itself acts as the single source of truth.
- **Immediate Day-Zero Support**: All new Azure services and API versions are immediately supported on launch day.
- **First-Class Modularization**: Clean, reusable modules with strong typing and parameter verification.
- **Seamless Decompilation**: Convert legacy ARM templates into readable Bicep in one command.

---

## 2. CLI Workflow & Commands

```bash
# Verify Bicep CLI is installed and check version
az bicep version

# Upgrade Bicep to latest release
az bicep upgrade

# Validate template syntax and compile to ARM JSON without deploying
az bicep build --file main.bicep

# Decompile an existing ARM JSON template into clean Bicep syntax
az bicep decompile --file azuredeploy.json

# Run a Preflight "What-If" diff (equivalent to terraform plan)
az deployment group what-if \
  --resource-group rg-analytics-prod \
  --template-file main.bicep \
  --parameters environment=prod location=eastus

# Deploy at Resource Group Scope
az deployment group create \
  --name "deploy-lakehouse-$(date +%Y%m%d-%H%M)" \
  --resource-group rg-analytics-prod \
  --template-file main.bicep \
  --parameters @main.bicepparam

# Deploy at Subscription Scope (e.g. creating Resource Groups & Role Assignments)
az deployment sub create \
  --name "deploy-landing-zone" \
  --location eastus \
  --template-file sub-main.bicep
```

---

## 3. Syntax Fundamentals & Decorators

Decorators validate inputs at compile and pre-flight phases:

```bicep
@description('Deployment target tier')
@allowed([
  'dev'
  'staging'
  'prod'
])
param environment string = 'dev'

@description('Primary deployment Azure region')
param location string = resourceGroup().location

@description('Storage Account SKU selection')
param storageSku string = environment == 'prod' ? 'Standard_ZRS' : 'Standard_LRS'

@description('Application administrator secret password')
@secure()
param adminPassword string

@description('Tags required by enterprise FinOps policy')
param tags object = {
  Environment: environment
  ManagedBy: 'Bicep'
  Project: 'EnterpriseLakehouse'
}
```

---

## 4. Parameters, Variables & Outputs

```bicep
// Variables for deterministic string interpolation
var cleanNamePrefix = toLower(replace('lake${environment}${location}', '-', ''))
var storageAccountName = '${take(cleanNamePrefix, 20)}${uniqueString(resourceGroup().id)}'

// Output values for downstream modules or CI/CD pipelines
output storageId string = storageAccount.id
output storageName string = storageAccount.name
output blobEndpoint string = storageAccount.properties.primaryEndpoints.blob
```

---

## 5. Modules & Composition

Break complex architectures into reusable modules (`infra/modules/storage.bicep`):

```bicep
// main.bicep invoking a child module
module dataLakeModule './modules/storage.bicep' = {
  name: 'deploy-adls-gen2'
  params: {
    accountName: storageAccountName
    location: location
    tags: tags
    enableHns: true
  }
}

// Module invocation output passing
output lakeEndpoint string = dataLakeModule.outputs.blobEndpoint
```

---

## 6. Loops & Conditionals

```bicep
param containerNames array = [
  'bronze'
  'silver'
  'gold'
  'checkpoints'
]

param deployMonitoringAlerts bool = environment == 'prod'

// Loop creating multiple ADLS containers
resource blobContainers 'Microsoft.Storage/storageAccounts/blobServices/containers@2023-05-01' = [for name in containerNames: {
  name: '${storageAccount.name}/default/${name}'
}]

// Conditional deployment (only in production)
resource diagnosticSettings 'Microsoft.Insights/diagnosticSettings@2021-05-01-preview' = if (deployMonitoringAlerts) {
  name: 'law-diagnostics'
  scope: storageAccount
  properties: {
    workspaceId: logAnalyticsWorkspaceId
    logs: [
      {
        categoryGroup: 'allLogs'
        enabled: true
      }
    ]
  }
}
```

---

## 7. Referencing Existing Resources

Reference pre-existing infrastructure (e.g., shared Hub VNets or Key Vaults) without modifying or re-creating them:

```bicep
// Reference shared Hub Virtual Network
resource hubVnet 'Microsoft.Network/virtualNetworks@2023-09-01' existing = {
  name: 'vnet-hub-core'
  scope: resourceGroup('rg-network-core')
}

// Reference shared Log Analytics Workspace
resource sharedLogAnalytics 'Microsoft.OperationalInsights/workspaces@2022-10-01' existing = {
  name: 'law-shared-prod'
  scope: resourceGroup('rg-monitoring-prod')
}
```

---

## 8. Secrets & Key Vault Integration

Never hardcode credentials! Read existing secrets directly inside Bicep:

```bicep
resource keyVault 'Microsoft.KeyVault/vaults@2023-07-01' existing = {
  name: 'kv-core-prod-01'
}

// Fetch secret securely at deploy time
var dbMasterPassword = keyVault.getSecret('DatabaseMasterPassword')
```

---

## 9. RBAC Role Assignments in Bicep

Assign Azure RBAC roles deterministically using unique GUID generation:

```bicep
param principalId string

// Built-in Storage Blob Data Contributor Role ID: ba92f5b4-2d11-453d-a403-e96b0029c9fe
var blobDataContributorRoleId = 'ba92f5b4-2d11-453d-a403-e96b0029c9fe'

resource roleAssignment 'Microsoft.Authorization/roleAssignments@2022-04-01' = {
  name: guid(storageAccount.id, principalId, blobDataContributorRoleId)
  scope: storageAccount
  properties: {
    roleDefinitionId: subscriptionResourceId('Microsoft.Authorization/roleDefinitions', blobDataContributorRoleId)
    principalId: principalId
    principalType: 'ServicePrincipal'
  }
}
```

---

## 10. Production Example: Storage + Private Endpoint + Key Vault

```bicep
@description('Deployment Environment')
param environment string = 'prod'
param location string = resourceGroup().location

// 1. ADLS Gen2 Storage Account
resource storageAccount 'Microsoft.Storage/storageAccounts@2023-05-01' = {
  name: 'stlake${environment}${uniqueString(resourceGroup().id)}'
  location: location
  sku: {
    name: 'Standard_ZRS'
  }
  kind: 'StorageV2'
  properties: {
    isHnsEnabled: true
    minimumTlsVersion: 'TLS1_2'
    supportsHttpsTrafficOnly: true
    allowBlobPublicAccess: false
    publicNetworkAccess: 'Disabled' // Zero Public Access
  }
}

// 2. Azure Key Vault with RBAC
resource keyVault 'Microsoft.KeyVault/vaults@2023-07-01' = {
  name: 'kv-${environment}-${uniqueString(resourceGroup().id)}'
  location: location
  properties: {
    sku: {
      family: 'A'
      name: 'standard'
    }
    tenantId: subscription().tenantId
    enableRbacAuthorization: true
    enableSoftDelete: true
    softDeleteRetentionInDays: 90
    publicNetworkAccess: 'Disabled'
  }
}
```

---

## 11. Azure Developer CLI (`azd`) Fast Track

`azd` provides a standardized template specification (`azure.yaml`) for rapid application scaffolding and deployment:

```bash
# Initialize a new azd project from template
azd init -t azure-samples/todo-python-mongo

# Log in to Azure Developer CLI
azd auth login

# Provision infrastructure (Bicep) and deploy code in a single command
azd up

# Inspect environment variables and provisioned outputs
azd env get-values

# View deployed application telemetry in Azure Portal
azd monitor --overview

# Teardown all resources provisioned by the template
azd down --purge
```

---

[← Back to Main Cheat Sheet](../README.md)
