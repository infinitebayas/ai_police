from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
import os


def _parse_bool(value: str | None, default: bool) -> bool:
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "on"}


def _parse_csv(value: str | None, default: tuple[str, ...]) -> tuple[str, ...]:
    if value is None or not value.strip():
        return default
    return tuple(item.strip() for item in value.split(",") if item.strip())


def _normalize_base_path(value: str | None) -> str:
    if value is None:
        return ""
    cleaned = value.strip()
    if not cleaned or cleaned == "/":
        return ""
    if not cleaned.startswith("/"):
        cleaned = f"/{cleaned}"
    return cleaned.rstrip("/")


def _load_dotenv(path: Path) -> None:
    if not path.exists():
        return
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        os.environ.setdefault(key, value)


@dataclass(slots=True)
class RuntimeSettings:
    app_name: str
    app_version: str
    host: str
    port: int
    base_path: str
    cors_origins: tuple[str, ...]
    profile_dir: Path
    web_dir: Path
    enable_ui: bool
    log_level: str
    database_url: str | None
    database_echo: bool
    database_auto_init: bool

    @classmethod
    def from_mapping(cls, mapping: dict[str, str], repo_root: Path) -> "RuntimeSettings":
        profile_dir = Path(mapping.get("AI_POLICE_PROFILE_DIR", "jurisdiction-profiles"))
        web_dir = Path(mapping.get("AI_POLICE_WEB_DIR", "web"))
        if not profile_dir.is_absolute():
            profile_dir = repo_root / profile_dir
        if not web_dir.is_absolute():
            web_dir = repo_root / web_dir
        return cls(
            app_name=mapping.get("AI_POLICE_APP_NAME", "AI Police API"),
            app_version=mapping.get("AI_POLICE_APP_VERSION", "0.1.0"),
            host=mapping.get("AI_POLICE_HOST", "127.0.0.1"),
            port=int(mapping.get("AI_POLICE_PORT", "8000")),
            base_path=_normalize_base_path(mapping.get("AI_POLICE_BASE_PATH")),
            cors_origins=_parse_csv(mapping.get("AI_POLICE_CORS_ORIGINS"), ("*",)),
            profile_dir=profile_dir,
            web_dir=web_dir,
            enable_ui=_parse_bool(mapping.get("AI_POLICE_ENABLE_UI"), True),
            log_level=mapping.get("AI_POLICE_LOG_LEVEL", "info"),
            database_url=mapping.get("AI_POLICE_DATABASE_URL") or None,
            database_echo=_parse_bool(mapping.get("AI_POLICE_DATABASE_ECHO"), False),
            database_auto_init=_parse_bool(mapping.get("AI_POLICE_DATABASE_AUTO_INIT"), False),
        )


@lru_cache(maxsize=1)
def get_settings() -> RuntimeSettings:
    repo_root = Path(__file__).resolve().parents[2]
    dotenv_path = repo_root / ".env"
    _load_dotenv(dotenv_path)
    env_map = dict(os.environ.items())
    return RuntimeSettings.from_mapping(env_map, repo_root)
