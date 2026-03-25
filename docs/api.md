# API Reference

This API exposes the same profile-aware assessment flow used by the CLI.

## Local Run

- `copy .env.example .env` or `cp .env.example .env`
- `python -m pip install -e .[api]`
- `python -m ai_police serve`

The default local address is `http://127.0.0.1:8000`.

## Endpoints

### `GET /health`

Returns service status.

Example response:

```json
{
  "status": "ok"
}
```

### `GET /profiles`

Returns the available jurisdiction profiles.

### `GET /profiles/{profile_name}`

Returns one profile by file stem.

Example:

- `GET /profiles/us-support`

### `POST /recommend`

Generate a support-first recommendation.

Example request:

```json
{
  "profile_name": "us-support",
  "case": {
    "jurisdiction": "US",
    "summary": "A school receives a report of repeated cyberbullying affecting a student after school hours.",
    "involves_child": true,
    "cyberbullying_indicator": true,
    "tags": ["school", "cyberbullying", "youth-safety"]
  }
}
```

The response includes profile details, normalized case data, recommendation output, and an audit record.

When database persistence is enabled, responses also include a `record_id` field.

### `GET /ready`

Returns runtime readiness details including profile directory presence, UI status, and base path.

## UI Serving

The FastAPI app also serves the lightweight UI at `/` and static assets under `/assets`.

When `AI_POLICE_BASE_PATH` is set, the UI and API stay aligned to that subpath.

## Deployment Note

This API is a public-interest support baseline. Production use should add authentication, access control, rate limiting, logging review, and privacy-approved persistence rules.

For institutional or government-friendly hosting discussions, see `government-readiness.md` and `certification-and-compliance.md`.
