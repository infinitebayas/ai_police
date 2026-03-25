from ai_police.config import load_profile
from ai_police.models import ReviewChannel


def test_load_profile_parses_review_channels() -> None:
    profile = load_profile("jurisdiction-profiles/us-support.json")

    assert profile.name == "United States Support Profile"
    assert ReviewChannel.SCHOOL_OR_COMMUNITY in profile.allowed_review_channels
    assert profile.require_human_review_for_all is True
