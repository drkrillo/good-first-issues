import pytest
from app.tests.conftest import mock_session

from app.api_handler import (
    APIClient,
    RepoManager,
    IssueManager,
    Utils,
)
from unittest.mock import Mock, patch
import requests

class TestUtils:

    def test_utils_divide_and_round_up(self):
        result = Utils().divide_and_round_up(150, 100)
        assert result == 2

    def test_utils_create_list_from_lists(self):
        nested_list = [[1, 2, 3], [4, 5, 6], None, [7, 8]]
        result = Utils().create_list_from_lists(nested_list)
        assert result == [1, 2, 3, 4, 5, 6, 7, 8]

class TestAPIClient:
        def test_apiclient_make_request_success(self): 
            url = "http://testurl.com"
            mock_response = mock_session.get.return_value
            mock_response.raise_for_status.return_value = None
            mock_response.json.return_value = {"message": "success"}

            # Llamar al método a probar
            result = APIClient.make_request(url, mock_session)
            
            # Validar el resultado
            assert result == {"message": "success"}
            mock_session.get.assert_called_once_with(url)

