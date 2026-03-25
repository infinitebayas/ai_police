# Local Verification Guide

This guide is the substitute for a live hosted environment when you want confidence before public release.

## Why This Matters

You do not need a live server to prove the repository is usable. You need a reproducible local verification path.

## Minimum Verification Set

### 1. Tests

```bash
python -m pytest
```

### 2. Runtime Settings

```bash
python -m ai_police show-settings
```

### 3. CLI Recommendation

```bash
python -m ai_police recommend --profile jurisdiction-profiles/us-support.json --case examples/cases/us-school-cyberbullying.json --include-audit
```

### 4. API Startup

```bash
python -m pip install -e .[api]
python -m ai_police serve
```

Then check:

- `GET /health`
- `GET /ready`
- `GET /profiles`
- browser UI at `/`

### 5. Schema Export Validation

```bash
python -m ai_police export-schema --dialect postgresql
python -m ai_police export-schema --dialect mysql
python -m ai_police export-schema --dialect mariadb
```

### 6. Preflight Script

```bash
python scripts/preflight.py
```

## Optional Database Verification

If you have a local database available, set `AI_POLICE_DATABASE_URL` in `.env` and run:

```bash
python -m ai_police init-db
```

Then re-run the CLI recommendation command and verify a `record_id` appears in the output.

## Result

If all of the above pass, the repository is in a credible publish-ready state even without a live host.
