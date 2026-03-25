from ai_police.audit import build_audit_record
from ai_police.models import CaseContext, RecommendationTier, ReviewChannel
from ai_police.triage import TriageEngine


def test_imminent_threat_routes_to_emergency_review() -> None:
    engine = TriageEngine()
    case = CaseContext(jurisdiction="US", summary="Direct threat reported", imminent_threat=True)

    recommendation = engine.recommend(case)

    assert recommendation.tier is RecommendationTier.SUPERVISED_ESCALATION
    assert recommendation.review_channel is ReviewChannel.EMERGENCY_REVIEW
    assert recommendation.requires_human_review is True


def test_child_exploitation_routes_to_welfare_support() -> None:
    engine = TriageEngine()
    case = CaseContext(
        jurisdiction="India",
        summary="Possible child exploitation report",
        involves_child=True,
        exploitation_indicator=True,
    )

    recommendation = engine.recommend(case)

    assert recommendation.tier is RecommendationTier.SUPERVISED_ESCALATION
    assert recommendation.review_channel is ReviewChannel.WELFARE_OR_SUPPORT


def test_cyberbullying_routes_to_school_or_community() -> None:
    engine = TriageEngine()
    case = CaseContext(
        jurisdiction="US",
        summary="School cyberbullying complaint",
        cyberbullying_indicator=True,
    )

    recommendation = engine.recommend(case)

    assert recommendation.tier is RecommendationTier.SUPPORT
    assert recommendation.review_channel is ReviewChannel.SCHOOL_OR_COMMUNITY


def test_audit_record_is_serializable_shape() -> None:
    engine = TriageEngine()
    case = CaseContext(jurisdiction="Global", summary="General support request")

    recommendation = engine.recommend(case)
    record = build_audit_record(case, recommendation)

    assert "created_at" in record
    assert record["case"]["jurisdiction"] == "Global"
    assert record["recommendation"]["tier"] == RecommendationTier.MONITOR.value
