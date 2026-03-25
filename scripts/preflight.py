from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    ROOT / "README.md",
    ROOT / "LICENSE",
    ROOT / "CONTACT.md",
    ROOT / ".env.example",
    ROOT / "pyproject.toml",
    ROOT / "src" / "ai_police" / "api.py",
    ROOT / "src" / "ai_police" / "cli.py",
    ROOT / "src" / "ai_police" / "database.py",
    ROOT / "web" / "index.html",
    ROOT / "db" / "schema" / "postgresql.sql",
    ROOT / "db" / "schema" / "mysql.sql",
    ROOT / "db" / "schema" / "mariadb.sql",
    ROOT / "docs" / "deployment-options.md",
    ROOT / "docs" / "database-support.md",
    ROOT / "docs" / "github-publish-checklist.md",
    ROOT / ".github" / "workflows" / "ci.yml",
    ROOT / ".github" / "workflows" / "release.yml",
]


def main() -> int:
    missing = [path for path in REQUIRED_FILES if not path.exists()]
    if missing:
        print("Preflight failed. Missing files:")
        for path in missing:
            print(f"- {path}")
        return 1

    print("Preflight passed.")
    print(f"Checked {len(REQUIRED_FILES)} required files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
