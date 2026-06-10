import pytest
import requests

@pytest.fixture
def mock_session(mocker):
    return mocker.Mock(spec=requests.Session)

@pytest.fixture
def mock_env_vars(monkeypatch):
    monkeypatch.setenv("GITHUB_TOKEN", "fake_token")
    monkeypatch.setenv("ORGANIZATIONS", "fake_org")