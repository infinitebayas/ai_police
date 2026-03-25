# Runtime Configuration

AI Police is designed to be environment-driven so the same codebase can run on:

- a root domain,
- a subdomain,
- a folder or subpath under an existing domain,
- a Linux VPS,
- container platforms,
- Azure and other cloud environments.

## Configuration Strategy

Use these layers together:

- `.env` for environment-specific runtime values,
- `jurisdiction-profiles/*.json` for policy and routing behavior,
- deployment-specific files for reverse proxy, systemd, container, or cloud wiring.

## Supported Environment Variables

- `AI_POLICE_APP_NAME`
- `AI_POLICE_APP_VERSION`
- `AI_POLICE_HOST`
- `AI_POLICE_PORT`
- `AI_POLICE_BASE_PATH`
- `AI_POLICE_CORS_ORIGINS`
- `AI_POLICE_PROFILE_DIR`
- `AI_POLICE_WEB_DIR`
- `AI_POLICE_ENABLE_UI`
- `AI_POLICE_LOG_LEVEL`
- `AI_POLICE_DATABASE_URL`
- `AI_POLICE_DATABASE_ECHO`
- `AI_POLICE_DATABASE_AUTO_INIT`

## Base Path Examples

### Root domain

```env
AI_POLICE_BASE_PATH=
```

### Subdomain

```env
AI_POLICE_BASE_PATH=
```

### Folder or subpath deployment

```env
AI_POLICE_BASE_PATH=/ai-police
```

This is useful when the application must live at paths such as:

- `https://example.org/ai-police`
- `https://portal.example.gov/tools/ai-police`

## Example Files

- `.env.example`
- `examples/env/general.env.example`
- `examples/env/vps.env.example`
- `examples/env/subpath.env.example`
- `examples/env/azure.env.example`

## CLI Support

The runtime settings can be inspected directly:

- `python -m ai_police show-settings`

The local API server also reads `.env` automatically:

- `python -m ai_police serve`

Database schema can also be initialized from the same configuration:

- `python -m ai_police init-db`

## Recommendation

Keep secrets and environment-specific values out of Git. Commit only examples and templates.
