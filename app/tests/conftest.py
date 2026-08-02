import pytest
import requests


@pytest.fixture
def mock_session(mocker):
    return mocker.Mock(spec=requests.Session)


@pytest.fixture
def mock_env_vars(monkeypatch):
    monkeypatch.setattr('app.update_issues.HEADERS', {'Authorization': 'Bearer test-token'})
    monkeypatch.setattr('app.update_issues.USERNAMES', ['test_user'])