from ai_police.config import load_profile
from ai_police.models import CaseContext, RecommendationTier, ReviewChannel
from ai_police.service import AssessmentService


def test_profile_fallback_uses_allowed_channel() -> None:
    profile = load_profile("jurisdiction-profiles/india-support.json")
    case = CaseContext(
        jurisdiction="India",
        summary="School cyberbullying report",
        cyberbullying_indicator=True,
    )

    result = AssessmentService().assess(case, profile)

    assert result.recommendation.tier is RecommendationTier.SUPPORT
    assert result.recommendation.review_channel is ReviewChannel.WELFARE_OR_SUPPORT
    assert any("profile" in item.lower() for item in result.recommendation.rationale)


def test_public_nodal_support_adds_review_action() -> None:
    profile = load_profile("jurisdiction-profiles/india-support.json")
    case = CaseContext(
        jurisdiction="India",
        summary="Harassment report from nodal channel",
        involves_woman=True,
        harassment_indicator=True,
        requested_by_public_nodal_support=True,
    )

    result = AssessmentService().assess(case, profile)

    assert any("institutional reviewer" in item.lower() for item in result.recommendation.actions)
    assert result.audit_record["profile_name"] == profile.name
