# Deployment Options

AI Police is structured so communities can develop and deploy it in more than one way without rewriting core assessment logic.

## Supported Development and Deployment Paths

### 1. Local Python Workflow

Use this when contributors want the lightest setup.

Commands:

- `cp .env.example .env` or `copy .env.example .env`
- `python -m pip install -e .[dev]`
- `python -m pytest`
- `python -m ai_police recommend --profile jurisdiction-profiles/us-support.json --case examples/cases/us-school-cyberbullying.json --include-audit`

Best for:

- maintainers,
- researchers,
- local experimentation,
- CI-compatible scripting.

Optional database persistence is available through `.env` if a development or staging database exists.

### 2. API Server Workflow

Use this when teams want integrations, forms, or downstream services.

Commands:

- `cp .env.example .env` or `copy .env.example .env`
- `python -m pip install -e .[api]`
- `python -m ai_police serve`

Endpoints:

- `GET /health`
- `GET /profiles`
- `GET /profiles/{profile_name}`
- `POST /recommend`

Best for:

- internal tools,
- web frontends,
- public-interest service pilots,
- integration with external applications.

This path can persist assessment records when `AI_POLICE_DATABASE_URL` is configured.

### 3. Static UI + API Workflow

The repository includes a lightweight browser UI in `web/` served by the FastAPI app.

Best for:

- demonstrations,
- community review,
- quick form-based experimentation,
- onboarding non-Python contributors.

### 4. Container Workflow

Use this when teams want repeatable local and hosted deployments.

Commands:

- `cp .env.example .env` or `copy .env.example .env`
- `docker compose up --build`

Database-specific compose options are also available under `deploy/compose/` for PostgreSQL, MySQL, and MariaDB.

Best for:

- shared environments,
- demos,
- staging systems,
- cloud handoff to other teams.

### 5. GitHub Workflow Path

The repository includes:

- test workflow in `.github/workflows/ci.yml`
- container build workflow in `.github/workflows/container.yml`
- release workflow in `.github/workflows/release.yml`
- contribution templates in `.github/`

Best for:

- open-source collaboration,
- pull-request validation,
- release hardening,
- future package or image publishing.

Before a public GitHub launch, also review:

- `local-verification.md`
- `github-publish-checklist.md`
- `release-runbook.md`

## Government-Friendly Hosting Notes

For public-sector or institutional evaluations, also review:

- `government-readiness.md`
- `certification-and-compliance.md`
- `deploy-linux-vps.md`
- `deploy-azure.md`

These documents are intended to support internal review, sovereign hosting discussions, and environment hardening plans.

For database-specific setup and schema import, review `database-support.md`.

## Design Principle

Each path reuses the same support-first assessment service and jurisdiction profile model. That keeps logic portable across:

- command-line tools,
- APIs,
- browser interfaces,
- containers,
- future hosted environments.

## Root Domain, Subdomain, and Subpath Support

Use `.env` to switch deployment style without changing code:

- Root domain: leave `AI_POLICE_BASE_PATH` empty.
- Subdomain: leave `AI_POLICE_BASE_PATH` empty and bind the subdomain at the proxy or host level.
- Folder/subpath: set `AI_POLICE_BASE_PATH=/your-path` and use a matching reverse-proxy config.

## Recommended Next Extensions

- add package publishing for tagged releases,
- add a hosted docs site,
- add authentication and rate limits for real API deployments,
- add persistence only after privacy and retention rules are finalized.
