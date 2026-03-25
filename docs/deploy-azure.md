# Deploy on Azure

Azure is a practical option for enterprise and government-adjacent teams that need managed hosting, identity controls, logging integration, and regional deployment choices.

## Recommended Azure Paths

### 1. Azure App Service (Container)

Suitable when you want a managed web app experience with moderate operational overhead.

High-level flow:

1. Build the Docker image.
2. Push it to Azure Container Registry or another supported registry.
3. Create an App Service configured for containers.
4. Set environment variables and access controls.
5. Restrict inbound access as needed.

### 2. Azure Container Apps

Suitable when you want managed containers with flexible scaling and modern container deployment workflows.

High-level flow:

1. Build and push the image.
2. Create a resource group, registry, and container apps environment.
3. Deploy the container app using the example YAML in `deploy/azure/containerapp.yaml`.
4. Bind domain and network controls if required.

### 3. Internal or Government-Controlled Azure Landing Zone

Suitable when the deployment must conform to existing governance, policy, network, and logging controls.

This usually means:

- managed identity,
- private networking,
- Key Vault-managed secrets,
- Log Analytics / Azure Monitor integration,
- policy and tagging requirements,
- resource locks and review approvals.

## Basic Azure CLI Flow

This repository does not assume one mandatory Azure product. A typical path looks like:

```bash
az group create --name ai-police-rg --location centralindia
az acr create --resource-group ai-police-rg --name aipoliceregistry --sku Basic
az acr build --registry aipoliceregistry --image ai-police:latest .
```

Then deploy the image to App Service or Container Apps.

Map runtime configuration from `.env.example` into Azure application settings or container environment variables. Use `examples/env/azure.env.example` as the starting point.

## Azure-Specific Readiness Controls

Recommended controls for serious deployments:

- Azure RBAC with least privilege
- Key Vault for secrets
- Defender for Cloud or equivalent review
- Private endpoints where required
- encrypted storage and backups
- regional deployment policy
- logging, metrics, and alert rules

## Documentation to Prepare

Before an institutional Azure deployment, prepare:

- environment ownership,
- network topology,
- resource inventory,
- secrets strategy,
- logging and retention policy,
- incident response runbook,
- scaling and failover expectations.
