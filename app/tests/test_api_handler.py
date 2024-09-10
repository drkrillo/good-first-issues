import pytest
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
    @patch('app.api_handler.requests.Session.get')
    def test_apiclient_make_request_success(self, mock_get):
        mock_response = Mock()
        mock_response.raise_for_status.return_value = None
        mock_response.json.return_value = {
            'mocked_key': 'mocked_value',
        }
        mock_get.return_value = mock_response
        
        session = requests.Session()
        url = 'http://www.mock-url.com'
        result = APIHandler()._make_request(url, session)
        
        assert result == {'mocked_key': 'mocked_value'}
    
    @patch('app.api_handler.requests.Session.get')
    def test_apiclient_make_request_error(self, mock_get):
        pass

