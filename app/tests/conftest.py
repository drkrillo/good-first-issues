import pytest
import requests

@pytest.fixture
def mock_session(mocker):
    return mocker.Mock(spec=requests.Session)

@pytest.fixture
def mock_env_vars(monkeypatch):
    monkeypatch.setenv("ACCESS_TOKEN", "fake_token_12345")
    monkeypatch.setenv("USERNAMES", "owner")