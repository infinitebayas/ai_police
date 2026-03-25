from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path

from .models import ReviewChannel


@dataclass(slots=True)
class JurisdictionProfile:
    name: str
    mode: str = "support-first"
    allowed_review_channels: tuple[ReviewChannel, ...] = field(
        default_factory=lambda: (
            ReviewChannel.PLATFORM,
            ReviewChannel.SCHOOL_OR_COMMUNITY,
            ReviewChannel.WELFARE_OR_SUPPORT,
            ReviewChannel.AGENCY_REVIEW,
            ReviewChannel.EMERGENCY_REVIEW,
        )
    )
    require_human_review_for_all: bool = True
    crisis_sensitive: bool = False
    child_safety_priority: bool = True
    women_safety_priority: bool = True
    public_nodal_support_enabled: bool = False
    support_resources: dict[str, str] = field(default_factory=dict)
    notes: tuple[str, ...] = field(default_factory=tuple)

    @classmethod
    def from_dict(cls, payload: dict[str, object]) -> "JurisdictionProfile":
        channels = payload.get("allowed_review_channels", [])
        return cls(
            name=str(payload["name"]),
            mode=str(payload.get("mode", "support-first")),
            allowed_review_channels=tuple(ReviewChannel(item) for item in channels) or cls().allowed_review_channels,
            require_human_review_for_all=bool(payload.get("require_human_review_for_all", True)),
            crisis_sensitive=bool(payload.get("crisis_sensitive", False)),
            child_safety_priority=bool(payload.get("child_safety_priority", True)),
            women_safety_priority=bool(payload.get("women_safety_priority", True)),
            public_nodal_support_enabled=bool(payload.get("public_nodal_support_enabled", False)),
            support_resources={str(key): str(value) for key, value in dict(payload.get("support_resources", {})).items()},
            notes=tuple(str(item) for item in payload.get("notes", [])),
        )


def load_profile(path: str | Path) -> JurisdictionProfile:
    profile_path = Path(path)
    payload = json.loads(profile_path.read_text(encoding="utf-8"))
    return JurisdictionProfile.from_dict(payload)
