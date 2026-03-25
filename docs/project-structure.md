# Project Structure

Proposed structure for implementation handoff:

- src/: core implementation modules
- docs/: governance and technical documentation
- tests/: unit, integration, and policy-behavior tests
- lists/: public policy lexicons and reference lists
- jurisdiction-profiles/: regional adaptation packs
- examples/: configuration and deployment examples
- web/: static browser UI assets
- .github/: issue templates, PR templates, and workflows

## Current Scaffold

- `src/ai_police/models.py`: case and recommendation data models
- `src/ai_police/triage.py`: support-first routing logic
- `src/ai_police/config.py`: jurisdiction profile schema and loader
- `src/ai_police/service.py`: profile-aware assessment flow
- `src/ai_police/cli.py`: developer-facing command-line entrypoint
- `src/ai_police/api.py`: FastAPI app for HTTP integrations and browser UI serving
- `src/ai_police/web_models.py`: shared serializers for CLI and API outputs
- `src/ai_police/audit.py`: minimal audit record builder
- `tests/test_api.py`: API and UI smoke tests
- `pyproject.toml`: package and test configuration

## Design Guidance

- Keep jurisdiction logic modular.
- Keep engine adapters isolated.
- Keep audit logging cross-cutting and mandatory.
- Keep public nodal support permissions constrained by role.
