from fastapi.testclient import TestClient

from ai_police.api import app


client = TestClient(app)


def test_health_endpoint() -> None:
    response = client.get('/health')

    assert response.status_code == 200
    assert response.json() == {'status': 'ok'}


def test_ready_endpoint_reports_runtime_state() -> None:
    response = client.get('/ready')

    assert response.status_code == 200
    payload = response.json()
    assert payload['status'] == 'ok'
    assert 'base_path' in payload
    assert 'ui_enabled' in payload


def test_profiles_endpoint_lists_known_profiles() -> None:
    response = client.get('/profiles')

    assert response.status_code == 200
    profile_ids = {item['id'] for item in response.json()['profiles']}
    assert 'us-support' in profile_ids
    assert 'india-support' in profile_ids


def test_recommend_endpoint_returns_assessment() -> None:
    response = client.post(
        '/recommend',
        json={
            'profile_name': 'us-support',
            'case': {
                'jurisdiction': 'US',
                'summary': 'A student reports repeated cyberbullying.',
                'involves_child': True,
                'cyberbullying_indicator': True,
                'tags': ['school']
            }
        },
    )

    assert response.status_code == 200
    payload = response.json()
    assert payload['recommendation']['review_channel'] == 'school_or_community'
    assert payload['recommendation']['requires_human_review'] is True


def test_root_serves_html() -> None:
    response = client.get('/')

    assert response.status_code == 200
    assert 'text/html' in response.headers['content-type']
