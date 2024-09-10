import pytest
import requests

@pytest.fixture
def mock_session(mocker):
    return mocker.Mock(spec=requests.Session)