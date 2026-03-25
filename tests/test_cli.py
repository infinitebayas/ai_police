from __future__ import annotations

import json
from contextlib import redirect_stdout
from io import StringIO

from ai_police.cli import main


def test_validate_profile_cli_outputs_json(monkeypatch) -> None:
    buffer = StringIO()
    monkeypatch.setattr(
        "sys.argv",
        ["ai-police", "validate-profile", "--profile", "jurisdiction-profiles/us-support.json"],
    )

    with redirect_stdout(buffer):
        exit_code = main()

    payload = json.loads(buffer.getvalue())
    assert exit_code == 0
    assert payload["name"] == "United States Support Profile"


def test_recommend_cli_includes_audit(monkeypatch) -> None:
    buffer = StringIO()
    monkeypatch.setattr(
        "sys.argv",
        [
            "ai-police",
            "recommend",
            "--profile",
            "jurisdiction-profiles/us-support.json",
            "--case",
            "examples/cases/us-school-cyberbullying.json",
            "--include-audit",
        ],
    )

    with redirect_stdout(buffer):
        exit_code = main()

    payload = json.loads(buffer.getvalue())
    assert exit_code == 0
    assert payload["recommendation"]["review_channel"] == "school_or_community"
    assert "audit_record" in payload
