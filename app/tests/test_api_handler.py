import unittest
from app.api_handler import APIHandler 
from unittest.mock import Mock, patch
import requests

class TestAPIHandler(unittest.TestCase):

    def setUp(self):
        self.api_handler = APIHandler()

    def test_divide_and_round_up(self):
        result = self.api_handler.divide_and_round_up(150, 100)
        self.assertEqual(result, 2)

    def test_create_list_from_lists(self):
        nested_list = [[1, 2, 3], [4, 5, 6], None, [7, 8]]
        result = self.api_handler.create_list_from_lists(nested_list)
        self.assertEqual(result, [1, 2, 3, 4, 5, 6, 7, 8])

    def test_extract_issue_data(self):
        raw_issue = ('Python', {
            'repository_url': 'https://api.github.com/repos/python/cpython',
            'title': 'Example issue',
            'html_url': 'https://github.com/python/cpython/issues/1',
            'comments': 5
        })
        result = self.api_handler.extract_issue_data(raw_issue)
        self.assertEqual(result['repo'], 'python/cpython')
        self.assertEqual(result['language'], 'Python')
        self.assertEqual(result['title'], 'Example issue')
        self.assertEqual(result['url'], 'https://github.com/python/cpython/issues/1')
        self.assertEqual(result['comments'], 5)
    
    @patch('app.api_handler.requests.Session.get')
    def test_make_request_success(self, mock_get):
        mock_response = Mock()
        mock_response.raise_for_status.return_value = None
        mock_response.json.return_value = {
            'mocked_key': 'mocked_value',
        }
        mock_get.return_value = mock_response
        
        session = requests.Session()
        url = 'http://www.mock-url.com'
        result = APIHandler()._make_request(url, session)
        
        self.assertEqual(result, {'mocked_key': 'mocked_value'})

