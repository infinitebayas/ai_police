from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

from .config import load_profile
from .database import DatabaseStore
from .models import CaseContext
from .service import AssessmentService
from .settings import get_settings
from .web_models import serialize_profile, serialize_result

SETTINGS = get_settings()
STORE = DatabaseStore(SETTINGS.database_url, echo=SETTINGS.database_echo) if SETTINGS.database_url else None

if STORE is not None and SETTINGS.database_auto_init:
    STORE.init_schema()

app = FastAPI(
    title=SETTINGS.app_name,
    version=SETTINGS.app_version,
    description="Support-first assessment API for public-interest triage workflows.",
    root_path=SETTINGS.base_path,
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=list(SETTINGS.cors_origins),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if SETTINGS.enable_ui and SETTINGS.web_dir.exists():
    app.mount("/assets", StaticFiles(directory=str(SETTINGS.web_dir / "assets")), name="assets")


class CasePayload(BaseModel):
    jurisdiction: str
    summary: str
    involves_child: bool = False
    involves_woman: bool = False
    imminent_threat: bool = False
    exploitation_indicator: bool = False
    cyberbullying_indicator: bool = False
    harassment_indicator: bool = False
    crisis_context: bool = False
    evidence_available: bool = False
    requested_by_public_nodal_support: bool = False
    tags: list[str] = Field(default_factory=list)


class RecommendPayload(BaseModel):
    profile_name: str
    case: CasePayload


def _profile_path(profile_name: str) -> Path:
    path = SETTINGS.profile_dir / f"{profile_name}.json"
    if not path.exists():
        raise HTTPException(status_code=404, detail=f"Unknown profile: {profile_name}")
    return path


def _to_case_context(payload: CasePayload) -> CaseContext:
    return CaseContext(
        jurisdiction=payload.jurisdiction,
        summary=payload.summary,
        involves_child=payload.involves_child,
        involves_woman=payload.involves_woman,
        imminent_threat=payload.imminent_threat,
        exploitation_indicator=payload.exploitation_indicator,
        cyberbullying_indicator=payload.cyberbullying_indicator,
        harassment_indicator=payload.harassment_indicator,
        crisis_context=payload.crisis_context,
        evidence_available=payload.evidence_available,
        requested_by_public_nodal_support=payload.requested_by_public_nodal_support,
        tags=tuple(payload.tags),
    )


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/ready")
def ready() -> dict[str, object]:
    return {
        "status": "ok",
        "profile_dir_exists": SETTINGS.profile_dir.exists(),
        "web_dir_exists": SETTINGS.web_dir.exists(),
        "base_path": SETTINGS.base_path,
        "ui_enabled": SETTINGS.enable_ui,
        "database_enabled": SETTINGS.database_url is not None,
    }


@app.get("/profiles")
def list_profiles() -> dict[str, list[dict[str, str]]]:
    profiles: list[dict[str, str]] = []
    for path in sorted(SETTINGS.profile_dir.glob("*.json")):
        payload = json.loads(path.read_text(encoding="utf-8"))
        profiles.append({"id": path.stem, "name": str(payload.get("name", path.stem))})
    return {"profiles": profiles}


@app.get(
    "/profiles/{profile_name}",
    responses={404: {"description": "Profile not found"}},
)
def get_profile(profile_name: str) -> dict[str, Any]:
    profile = load_profile(_profile_path(profile_name))
    return {"profile": serialize_profile(profile)}


@app.post(
    "/recommend",
    responses={404: {"description": "Profile not found"}},
)
def recommend(payload: RecommendPayload) -> dict[str, Any]:
    profile = load_profile(_profile_path(payload.profile_name))
    case = _to_case_context(payload.case)
    result = AssessmentService(store=STORE).assess(case, profile)
    return serialize_result(result, profile, case)


@app.get(
    "/",
    responses={404: {"description": "Web UI not found"}},
)
def root() -> HTMLResponse:
    index_path = SETTINGS.web_dir / "index.html"
    if not SETTINGS.enable_ui or not index_path.exists():
        raise HTTPException(status_code=404, detail="Web UI not found")
    base_path = SETTINGS.base_path or ""
    html = index_path.read_text(encoding="utf-8")
    html = html.replace("__AI_POLICE_BASE_PATH__", base_path)
    html = html.replace("__AI_POLICE_APP_NAME__", SETTINGS.app_name)
    return HTMLResponse(html)
