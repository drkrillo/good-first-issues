import requests
import pytest
from unittest.mock import patch, MagicMock

from api_handler import (
    APIClient,
    RepoManager,
    IssueManager,
    Utils,
)
from exception_handler import APIError


class TestRepoManager:
        
    @patch('api_handler.APIClient')
    def test_extract_number_of_repos(self, mock_api_client):
        mock_api_instance = MagicMock()
        mock_api_client.return_value = mock_api_instance
        mock_api_instance.make_request.return_value = {'public_repos': 42}

        result = RepoManager().extract_number_of_repos('test_user', mock_api_instance)

        assert result == 42

class TestIssueManager:
    @patch('api_handler.APIClient')
    def test_extract_issue_data(self, mock_api_client):
        pass
    
class TestUtils:

    def test_utils_divide_and_round_up(self):
        result = Utils().divide_and_round_up(150, 100)
        assert result == 2

    def test_utils_create_list_from_lists(self):
        nested_list = [[1, 2, 3], [4, 5, 6], None, [7, 8]]
        result = Utils().create_list_from_lists(nested_list)
        assert result == [1, 2, 3, 4, 5, 6, 7, 8]

class TestAPIClient:
    
        def test_apiclient_make_request_success(self, mock_session): 
            url = "http://testurl.com"
            mock_response = mock_session.get.return_value
            mock_response.raise_for_status.return_value = None
            mock_response.json.return_value = {"message": "success"}

            # Llamar al método a probar
            result = APIClient.make_request(url, mock_session)
            
            # Validar el resultado
            assert result == {"message": "success"}
            mock_session.get.assert_called_once_with(url)

        def test_apiclient_make_request_error(self, mock_session): 
            url = "http://testurl.com"
            mock_response = mock_session.get.return_value
            mock_response.status_code = 404
            mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError
            mock_response.text = 'Not Found'
            
            with pytest.raises(APIError) as excinfo:
                APIClient.make_request(url, mock_session)
                            
            assert excinfo.value.status_code == 404
            assert excinfo.value.message == 'Not Found'

