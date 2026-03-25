from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class RecommendationTier(str, Enum):
    MONITOR = "monitor"
    SUPPORT = "support"
    SUPERVISED_ESCALATION = "supervised_escalation"


class ReviewChannel(str, Enum):
    PLATFORM = "platform"
    SCHOOL_OR_COMMUNITY = "school_or_community"
    WELFARE_OR_SUPPORT = "welfare_or_support"
    AGENCY_REVIEW = "agency_review"
    EMERGENCY_REVIEW = "emergency_review"


@dataclass(slots=True)
class CaseContext:
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
    tags: tuple[str, ...] = field(default_factory=tuple)


@dataclass(slots=True)
class Recommendation:
    tier: RecommendationTier
    review_channel: ReviewChannel
    rationale: list[str]
    actions: list[str]
    requires_human_review: bool = True
