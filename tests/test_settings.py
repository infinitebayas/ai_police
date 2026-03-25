from pathlib import Path

from ai_police.settings import RuntimeSettings


def test_runtime_settings_support_subpath_and_relative_dirs() -> None:
    repo_root = Path('D:/laragon/www/ai_police')
    settings = RuntimeSettings.from_mapping(
        {
            'AI_POLICE_APP_NAME': 'AI Police API',
            'AI_POLICE_HOST': '0.0.0.0',
            'AI_POLICE_PORT': '8010',
            'AI_POLICE_BASE_PATH': '/ai-police',
            'AI_POLICE_CORS_ORIGINS': 'https://example.org,https://sub.example.org',
            'AI_POLICE_PROFILE_DIR': 'jurisdiction-profiles',
            'AI_POLICE_WEB_DIR': 'web',
            'AI_POLICE_ENABLE_UI': 'true',
            'AI_POLICE_LOG_LEVEL': 'warning',
        },
        repo_root,
    )

    assert settings.host == '0.0.0.0'
    assert settings.port == 8010
    assert settings.base_path == '/ai-police'
    assert settings.cors_origins == ('https://example.org', 'https://sub.example.org')
    assert settings.profile_dir == repo_root / 'jurisdiction-profiles'
    assert settings.web_dir == repo_root / 'web'
    assert settings.enable_ui is True
    assert settings.log_level == 'warning'
