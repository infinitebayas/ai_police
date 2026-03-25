# AI Police

AI Police is a local-first, deployment-ready public-interest governance framework for AI-assisted moderation, auditable risk triage, and lawful escalation in digital public spaces.

The project is designed to support agencies, civic institutions, and approved operators with consistent guidance while remaining subordinate to applicable law, due process, and platform policies.

This repository is intended to be useful on first public release: it can be reviewed, tested, demonstrated locally, containerized, and adapted for institutional pilots before any live production rollout.

## Public Interest Mission

- Strengthen lawful, accountable digital governance.
- Support safe public communication spaces with AI-guided moderation workflows.
- Provide extensible moderation engines for local adaptation.
- Enable collaboration between public stakeholders, cyber units, and policing support functions.

## Authority Model

AI Police uses a hybrid authority model:

- Authoritative guidance by default: standardized policy interpretation, risk scoring, and escalation recommendations.
- Operational enforcement only under lawful operators: enforcement actions must be tied to authorized institutions and legal mandates.
- Jurisdiction-first deployment: local law and agency policy take precedence over default configuration.

## Repository Scope (Public)

Included:

- Governance and architecture guidance.
- Extensible moderation design patterns.
- Jurisdiction adaptation framework.
- Public safety and transparency documentation.

Excluded:

- Hidden political/private rule packs.
- Extra-legal enforcement claims.
- Unsupported production guarantees.

## Core Documentation

- [Architecture](docs/architecture.md)
- [Quickstart](docs/quickstart.md)
- [Configuration](docs/configuration.md)
- [Decision Logic](docs/decision-logic.md)
- [Jurisdiction Adaptation Matrix](docs/jurisdiction-adaptation-matrix.md)
- [Country Adaptation Notes](docs/country-adaptation-notes.md)
- [Social Risk Landscape](docs/social-risk-landscape.md)
- [Public-Interest Use Cases](docs/public-interest-use-cases.md)
- [Safeguards by Design](docs/safeguards-by-design.md)
- [Evaluation Metrics](docs/evaluation-metrics.md)
- [References](docs/references.md)
- [API Reference](docs/api.md)
- [Deployment Options](docs/deployment-options.md)
- [Runtime Configuration](docs/runtime-configuration.md)
- [Database Support](docs/database-support.md)
- [Local Verification](docs/local-verification.md)
- [GitHub Publish Checklist](docs/github-publish-checklist.md)
- [Release Runbook](docs/release-runbook.md)
- [Launch Kit](docs/launch-kit.md)
- [Public Note in Hindi](docs/public-note-hi.md)
- [Public Note in Marathi](docs/public-note-mr.md)
- [Public Note in Mexican Spanish](docs/public-note-es-mx.md)
- [Linux VPS Deployment](docs/deploy-linux-vps.md)
- [Azure Deployment](docs/deploy-azure.md)
- [Additional Platform Deployment](docs/deploy-platforms.md)
- [Government Readiness](docs/government-readiness.md)
- [Certification and Compliance Considerations](docs/certification-and-compliance.md)
- [Future Exploration](docs/future-exploration.md)
- [Roadmap](docs/roadmap.md)

## Governance and Trust

- [Privacy](PRIVACY.md)
- [Safety](SAFETY.md)
- [Ethical Guidelines](ETHICAL-GUIDELINES.md)
- [Security](SECURITY.md)
- [Police Departments Note](POLICE-DEPARTMENTS-NOTE.md)
- [Contact](CONTACT.md)

## Research and Safe Application

The repository now includes a non-operational research pack focused on public-interest application for women, children, and vulnerable civilians in:

- India,
- the United States,
- conflict-affected and humanitarian settings.

These materials are designed for support-first, referral-first, and audit-first deployment planning.

## Contributing

- [Contributing Guide](CONTRIBUTING.md)
- [Code of Conduct](CODE_OF_CONDUCT.md)
- [Maintenance](MAINTENANCE.md)
- [Changelog](CHANGELOG.md)

## Current Status

This repository now provides governance documentation plus a minimal Python scaffolding for support-first triage and auditable recommendations.

In practical terms, the current release state is:

- public-review ready,
- locally verifiable,
- API and UI runnable,
- container-ready,
- database-optional,
- prepared for first GitHub publication.

If you are landing on this repository for the first time, the fastest path is:

1. review the public scope and safeguards below,
2. run the local verification flow,
3. inspect the API, UI, and example profiles,
4. use the launch kit when publishing or sharing the project.

Current scaffolded components:

- Python package metadata in `pyproject.toml`
- support-first triage engine in `src/ai_police/triage.py`
- profile-aware assessment service in `src/ai_police/service.py`
- jurisdiction profile loader in `src/ai_police/config.py`
- CLI entrypoint in `src/ai_police/cli.py`
- FastAPI service in `src/ai_police/api.py`
- static browser UI in `web/`
- optional multi-database persistence in `src/ai_police/database.py`
- recommendation and case models in `src/ai_police/models.py`
- audit record builder in `src/ai_police/audit.py`
- automated tests in `tests/`
- publish preflight checker in `scripts/preflight.py`

## Quick CLI Example

Install locally:

- `python -m pip install -e .[dev]`

Copy the runtime template first when you want a local `.env` file:

- `copy .env.example .env` on Windows
- `cp .env.example .env` on Linux/macOS

Validate a profile:

- `python -m ai_police validate-profile --profile jurisdiction-profiles/us-support.json`

Generate a recommendation from an example case:

- `python -m ai_police recommend --profile jurisdiction-profiles/us-support.json --case examples/cases/us-school-cyberbullying.json --include-audit`

Run the publication preflight:

- `python scripts/preflight.py`

## API and UI Example

Run the API locally:

- `python -m pip install -e .[api]`
- `python -m ai_police serve`

Then open:

- `http://127.0.0.1:8000/` for the browser UI
- `http://127.0.0.1:8000/docs` for the generated API docs

## Container Example

- `copy .env.example .env` or `cp .env.example .env`
- `docker compose up --build`

This starts the same API and UI stack in a portable container workflow.

## Domain and Path Flexibility

This project is runtime-configurable for:

- root domain deployment,
- subdomain deployment,
- folder or subpath deployment.

Set `AI_POLICE_BASE_PATH` in `.env` when the app must live under a path such as `/ai-police`.

## Public and Institutional Contact

For all public, government, institutional, partnership, or implementation inquiries, use:

- [LinkedIn](https://www.linkedin.com/in/infinitebayas/)
- [X](https://x.com/InfiniteBayas)

For open-source collaboration, continue using GitHub issues and pull requests.

## Example Profiles and Cases

- `jurisdiction-profiles/india-support.json`
- `jurisdiction-profiles/us-support.json`
- `jurisdiction-profiles/conflict-civilian-protection.json`
- `examples/cases/india-women-harassment.json`
- `examples/cases/us-school-cyberbullying.json`
- `examples/cases/conflict-child-protection.json`

## Database Options

The app remains runnable without a database, but it now supports optional persistence for:

- PostgreSQL
- MySQL
- MariaDB

Use `.env` plus the schema files under `db/schema/` or the CLI command:

- `python -m ai_police init-db`
- `python -m ai_police export-schema --dialect postgresql`

Container-based database examples are included under `deploy/compose/` for PostgreSQL, MySQL, and MariaDB.

Production deployment should only proceed after:

- legal and policy review in the target jurisdiction,
- technical validation of moderation and escalation logic,
- human oversight controls and audit mechanisms are active.

If you are preparing the repository for a public GitHub launch without a live host yet, start with:

- [docs/local-verification.md](docs/local-verification.md)
- [docs/github-publish-checklist.md](docs/github-publish-checklist.md)
- [docs/release-runbook.md](docs/release-runbook.md)
- [docs/launch-kit.md](docs/launch-kit.md)

If Git has not been connected to GitHub yet, initialize the repository locally, create the GitHub repository, add the remote, and then follow the first-push sequence in `docs/release-runbook.md`.

## License

This repository is released under the MIT License. See LICENSE.
