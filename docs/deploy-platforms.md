# Additional Deployment Platforms

This repository is intentionally deployment-agnostic. The same core package can be adapted across multiple hosting styles.

## Community-Friendly Platform Options

### Render

Useful for quick public demos and API hosting.

### Railway

Useful for rapid container or Python service deployment with low setup friction.

### Fly.io

Useful for lightweight global deployments and container-first workflows.

### Generic VM or Bare Metal

Useful where sovereign control, on-premise hosting, or internal review constraints matter most.

### Kubernetes

Useful for organizations that already standardize on clusters, ingress, and policy-driven deployment.

## Design Guidance for Portable Deployments

To stay portable:

- keep configuration externalized,
- avoid provider-specific business logic,
- keep the core assessment layer stateless where possible,
- add persistence only after privacy and retention rules are approved,
- document profile files and environment variables clearly.

## Selection Questions

Choose a deployment path based on:

- who operates it,
- where data may reside,
- whether sovereign hosting is required,
- expected user volume,
- whether public access is needed,
- whether the environment needs internal-only access.
