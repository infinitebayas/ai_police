from __future__ import annotations

import argparse
import json
from dataclasses import asdict
from pathlib import Path
from typing import Any

from .config import JurisdictionProfile, load_profile
from .database import DatabaseStore, export_schema_sql
from .models import CaseContext
from .service import AssessmentService
from .settings import get_settings


def _load_case(path: str | Path) -> CaseContext:
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    tags = tuple(str(item) for item in payload.get("tags", []))
    return CaseContext(
        jurisdiction=str(payload["jurisdiction"]),
        summary=str(payload["summary"]),
        involves_child=bool(payload.get("involves_child", False)),
        involves_woman=bool(payload.get("involves_woman", False)),
        imminent_threat=bool(payload.get("imminent_threat", False)),
        exploitation_indicator=bool(payload.get("exploitation_indicator", False)),
        cyberbullying_indicator=bool(payload.get("cyberbullying_indicator", False)),
        harassment_indicator=bool(payload.get("harassment_indicator", False)),
        crisis_context=bool(payload.get("crisis_context", False)),
        evidence_available=bool(payload.get("evidence_available", False)),
        requested_by_public_nodal_support=bool(payload.get("requested_by_public_nodal_support", False)),
        tags=tags,
    )


def _serialize_profile(profile: JurisdictionProfile) -> dict[str, Any]:
    data = asdict(profile)
    data["allowed_review_channels"] = [channel.value for channel in profile.allowed_review_channels]
    return data


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="ai-police")
    subparsers = parser.add_subparsers(dest="command", required=True)

    recommend = subparsers.add_parser("recommend", help="Generate a support-first recommendation")
    recommend.add_argument("--profile", required=True, help="Path to a jurisdiction profile JSON file")
    recommend.add_argument("--case", required=True, help="Path to a case JSON file")
    recommend.add_argument("--include-audit", action="store_true", help="Include audit record in output")

    validate = subparsers.add_parser("validate-profile", help="Validate and print a jurisdiction profile")
    validate.add_argument("--profile", required=True, help="Path to a jurisdiction profile JSON file")

    subparsers.add_parser("show-settings", help="Print resolved runtime settings")

    subparsers.add_parser("serve", help="Run the local API server using .env-aware settings")

    init_db = subparsers.add_parser("init-db", help="Initialize the configured database schema")
    init_db.add_argument("--url", help="Override AI_POLICE_DATABASE_URL for this command")

    export_schema = subparsers.add_parser("export-schema", help="Print SQL schema for a target database dialect")
    export_schema.add_argument("--dialect", choices=["postgresql", "mysql", "mariadb"], required=True)

    return parser


def _settings_payload() -> dict[str, Any]:
    settings = get_settings()
    return {
        "app_name": settings.app_name,
        "app_version": settings.app_version,
        "host": settings.host,
        "port": settings.port,
        "base_path": settings.base_path,
        "cors_origins": settings.cors_origins,
        "profile_dir": str(settings.profile_dir),
        "web_dir": str(settings.web_dir),
        "enable_ui": settings.enable_ui,
        "log_level": settings.log_level,
        "database_url": settings.database_url,
        "database_echo": settings.database_echo,
        "database_auto_init": settings.database_auto_init,
    }


def _build_store() -> DatabaseStore | None:
    settings = get_settings()
    if not settings.database_url:
        return None
    store = DatabaseStore(settings.database_url, echo=settings.database_echo)
    if settings.database_auto_init:
        store.init_schema()
    return store


def _handle_validate_profile(args: argparse.Namespace) -> int:
    profile = load_profile(args.profile)
    print(json.dumps(_serialize_profile(profile), indent=2))
    return 0


def _handle_show_settings(_: argparse.Namespace) -> int:
    print(json.dumps(_settings_payload(), indent=2))
    return 0


def _handle_recommend(args: argparse.Namespace) -> int:
    profile = load_profile(args.profile)
    case = _load_case(args.case)
    service = AssessmentService(store=_build_store())
    result = service.assess(case, profile)
    output: dict[str, Any] = {
        "profile": _serialize_profile(profile),
        "case": asdict(case),
        "recommendation": {
            "tier": result.recommendation.tier.value,
            "review_channel": result.recommendation.review_channel.value,
            "rationale": result.recommendation.rationale,
            "actions": result.recommendation.actions,
            "requires_human_review": result.recommendation.requires_human_review,
        },
    }
    if args.include_audit:
        output["audit_record"] = result.audit_record
    if result.record_id is not None:
        output["record_id"] = result.record_id
    print(json.dumps(output, indent=2))
    return 0


def _handle_init_db(args: argparse.Namespace) -> int:
    settings = get_settings()
    database_url = args.url or settings.database_url
    if not database_url:
        raise SystemExit("Set AI_POLICE_DATABASE_URL in .env or pass --url.")
    store = DatabaseStore(database_url, echo=settings.database_echo)
    store.init_schema()
    print(json.dumps({"status": "ok", "database_url": database_url}, indent=2))
    return 0


def _handle_export_schema(args: argparse.Namespace) -> int:
    print(export_schema_sql(args.dialect))
    return 0


def _handle_serve(_: argparse.Namespace) -> int:
    settings = get_settings()
    try:
        import uvicorn
    except ImportError as exc:
        raise SystemExit("Install the API extras first: python -m pip install -e .[api]") from exc

    uvicorn.run(
        "ai_police.api:app",
        host=settings.host,
        port=settings.port,
        log_level=settings.log_level,
    )
    return 0


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    handlers = {
        "validate-profile": _handle_validate_profile,
        "show-settings": _handle_show_settings,
        "recommend": _handle_recommend,
        "init-db": _handle_init_db,
        "export-schema": _handle_export_schema,
        "serve": _handle_serve,
    }
    handler = handlers.get(args.command)
    if handler is None:
        parser.error("Unknown command")
        return 2
    return handler(args)


if __name__ == "__main__":
    raise SystemExit(main())
