# Development

This repository is currently documentation-first. Development should proceed in controlled phases.

The repository now includes a minimal Python scaffold for:

- case intake models,
- support-first triage recommendations,
- jurisdiction profile loading,
- profile-aware assessment service,
- API endpoints,
- static web interface assets,
- audit record creation,
- baseline test coverage.

## Runtime Configuration First

Use `.env` for environment-specific deployment values and keep jurisdiction behavior in `jurisdiction-profiles/*.json`.

Start from `.env.example` and adjust:

- host and port,
- CORS origins,
- base path,
- profile directory,
- UI enablement,
- database URL and schema behavior.

## Development Principles

- Build for legal adaptability.
- Keep decision paths explainable.
- Preserve auditability and rollback points.
- Separate policy logic from model implementation.

## Suggested Build Phases

1. Interfaces and contracts
2. Retrieval and policy ingestion
3. Engine integration adapters
4. Escalation orchestrator
5. Audit trail and review tooling
6. Safety and misuse tests

## Local Commands

- `python -m pip install -e .[dev]`
- `pytest`
- `python -m ai_police show-settings`
- `python -m ai_police init-db`
- `python -m ai_police export-schema --dialect postgresql`
- `python -m ai_police validate-profile --profile jurisdiction-profiles/us-support.json`
- `python -m ai_police recommend --profile jurisdiction-profiles/us-support.json --case examples/cases/us-school-cyberbullying.json --include-audit`
- `python scripts/preflight.py`
- `python -m ai_police serve`
- `docker compose up --build`

## Release and Public Publishing Support

The repository now includes:

- CI workflow for tests
- container build workflow
- release build workflow for tagged versions
- deployment examples for Linux VPS and Azure

This makes the repo suitable for GitHub publication and for multiple downstream deployment styles.

Use these docs for release preparation:

- `docs/local-verification.md`
- `docs/github-publish-checklist.md`
- `docs/release-runbook.md`

## Definition of Done (Per Feature)

- behavior documented,
- risk documented,
- legal assumptions explicit,
- oversight checkpoints included,
- rollback path defined.
