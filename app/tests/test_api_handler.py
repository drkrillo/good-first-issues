import requests
import pytest
from unittest.mock import patch, MagicMock

from app.core.api_handler import (
    APIClient,
    RepoManager,
    IssueManager,
    Utils,
    TemplateManager,
)
from app.core.custom_exceptions import APIError


class TestRepoManager:
        
    @patch('app.core.api_handler.APIClient')
    def test_extract_number_of_repos(self, mock_api_client):
        mock_api_instance = MagicMock()
        mock_api_client.return_value = mock_api_instance
        mock_api_instance.make_request.return_value = {'public_repos': 42}

        result = RepoManager().extract_number_of_repos('test_user', mock_api_instance)

        assert result == 42

    @patch('app.core.api_handler.APIClient')
    @patch('app.core.api_handler.RepoManager.extract_number_of_repos')
    def test_extract_repos(self, mock_extract_number, mock_api_client):
        mock_api_instance = MagicMock()
        mock_api_client.return_value = mock_api_instance
        
        # Mock 150 repos which should result in 2 pages
        mock_extract_number.return_value = 150
        
        # Mock the response for each page
        mock_api_instance.make_request.side_effect = [
            [{"url": "https://api.github.com/repos/owner/repo1"},
             {"url": "https://api.github.com/repos/owner/repo2"}],
            [{"url": "https://api.github.com/repos/owner/repo3"}]
        ]

        result = RepoManager().extract_repos('test_user', mock_api_instance)

        assert len(result) == 3
        assert result == [
            "https://api.github.com/repos/owner/repo1",
            "https://api.github.com/repos/owner/repo2",
            "https://api.github.com/repos/owner/repo3"
        ]
        
        # Verify API calls
        assert mock_api_instance.make_request.call_count == 2
        mock_api_instance.make_request.assert_any_call(
            "https://api.github.com/users/test_user/repos?page=1&per_page=100",
            mock_api_instance
        )
        mock_api_instance.make_request.assert_any_call(
            "https://api.github.com/users/test_user/repos?page=2&per_page=100",
            mock_api_instance
        )

    @patch('app.core.api_handler.APIClient')
    def test_extract_number_of_repos_error(self, mock_api_client):
        mock_api_instance = MagicMock()
        mock_api_client.return_value = mock_api_instance
        mock_api_instance.make_request.return_value = {}  # Missing 'public_repos' key

        with pytest.raises(KeyError):
            RepoManager().extract_number_of_repos('test_user', mock_api_instance)

    @patch('app.core.api_handler.APIClient')
    @patch('app.core.api_handler.RepoManager.extract_number_of_repos')
    def test_extract_repos_error(self, mock_extract_number, mock_api_client):
        mock_api_instance = MagicMock()
        mock_api_client.return_value = mock_api_instance
        mock_extract_number.return_value = 1
        mock_api_instance.make_request.return_value = None  # Will cause TypeError

        with pytest.raises(TypeError):
            RepoManager().extract_repos('test_user', mock_api_instance)

class TestIssueManager:
    @patch('app.core.api_handler.APIClient')
    def test_extract_issue_data(self, mock_api_client):
        raw_issue = (
            "Python",
            {
                "repository_url": "https://api.github.com/repos/owner/repo",
                "title": "Test Issue",
                "html_url": "https://github.com/owner/repo/issues/1",
                "comments": 5
            }
        )
        
        result = IssueManager().extract_issue_data(raw_issue)
        
        assert result == {
            "repo": "owner/repo",
            "language": "Python",
            "title": "Test Issue",
            "url": "https://github.com/owner/repo/issues/1",
            "comments": 5
        }

    @patch('app.core.api_handler.APIClient')
    def test_extract_language(self, mock_api_client):
        mock_api_instance = MagicMock()
        mock_api_client.return_value = mock_api_instance
        mock_api_instance.make_request.return_value = {"language": "Python"}

        result = IssueManager().extract_language("https://api.github.com/repos/owner/repo", mock_api_instance)

        assert result == "Python"
        mock_api_instance.make_request.assert_called_once_with("https://api.github.com/repos/owner/repo", mock_api_instance)

    @patch('app.core.api_handler.APIClient')
    def test_extract_issues(self, mock_api_client):
        mock_api_instance = MagicMock()
        mock_api_client.return_value = mock_api_instance
        
        # Mock the language request
        mock_api_instance.make_request.side_effect = [
            {"language": "Python"},  # First call for extract_language
            [  # Second call for issues
                {
                    "title": "Test Issue",
                    "html_url": "https://github.com/owner/repo/issues/1",
                    "comments": 5
                }
            ]
        ]

        result = IssueManager().extract_issues("https://api.github.com/repos/owner/repo", mock_api_instance)

        assert len(result) == 1
        assert result[0][0] == "Python"  # Language
        assert result[0][1]["title"] == "Test Issue"
        
        # Verify API calls
        assert mock_api_instance.make_request.call_count == 2
        mock_api_instance.make_request.assert_any_call("https://api.github.com/repos/owner/repo", mock_api_instance)
        mock_api_instance.make_request.assert_any_call("https://api.github.com/repos/owner/repo/issues?labels=good first issue", mock_api_instance)

    @patch('app.core.api_handler.APIClient')
    def test_extract_issue_data_error(self, mock_api_client):
        raw_issue = (
            "Python",
            {
                # Missing required keys
                "repository_url": "https://api.github.com/repos/owner/repo"
            }
        )
        
        with pytest.raises(Exception):
            IssueManager().extract_issue_data(raw_issue)

    @patch('app.core.api_handler.APIClient')
    def test_extract_language_error(self, mock_api_client):
        mock_api_instance = MagicMock()
        mock_api_client.return_value = mock_api_instance
        mock_api_instance.make_request.return_value = {}  # Missing 'language' key

        with pytest.raises(KeyError):
            IssueManager().extract_language("https://api.github.com/repos/owner/repo", mock_api_instance)

    @patch('app.core.api_handler.APIClient')
    def test_extract_issues_error(self, mock_api_client):
        mock_api_instance = MagicMock()
        mock_api_client.return_value = mock_api_instance
        mock_api_instance.make_request.side_effect = [
            {"language": "Python"},  # First call for extract_language
            None  # Second call will cause TypeError
        ]

        with pytest.raises(TypeError):
            IssueManager().extract_issues("https://api.github.com/repos/owner/repo", mock_api_instance)

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

    def test_apiclient_make_request_general_error(self, mock_session):
        url = "http://testurl.com"
        mock_session.get.side_effect = Exception("General error")
        
        with pytest.raises(Exception) as excinfo:
            APIClient.make_request(url, mock_session)
            
        assert str(excinfo.value) == "General error"

class TestAPIError:
    def test_api_error_str(self):
        error = APIError(404, "Not Found")
        assert str(error) == "APIError 404: Not Found"

class TestTemplateManager:
    def test_format_response(self):
        issues = [
            {
                'language': 'Python',
                'title': 'Issue 1',
                'url': 'url1',
                'comments': 5,
                'repo': 'repo1'
            },
            {
                'language': 'Python',
                'title': 'Issue 2',
                'url': 'url2',
                'comments': 2,
                'repo': 'repo2'
            },
            {
                'language': 'JavaScript',
                'title': 'Issue 3',
                'url': 'url3',
                'comments': 3,
                'repo': 'repo3'
            }
        ]

        result = TemplateManager().format_response(issues)

        assert len(result) == 2  # Two languages
        
        # Check JavaScript issues
        js_result = next(r for r in result if r['language'] == 'JavaScript')
        assert len(js_result['issues']) == 1
        assert js_result['issues'][0]['title'] == 'Issue 3'

        # Check Python issues (should be sorted by comments)
        py_result = next(r for r in result if r['language'] == 'Python')
        assert len(py_result['issues']) == 2
        assert py_result['issues'][0]['comments'] == 2  # First should have fewer comments
        assert py_result['issues'][1]['comments'] == 5  # Second should have more comments

    def test_render_template(self, tmp_path):
        # Create a temporary template file
        template_dir = tmp_path / "templates"
        template_dir.mkdir()
        template_file = template_dir / "README.md.j2"
        template_content = """# Good First Issues ({{ today }})

{% for lang in results %}
## {{ lang.language }}
{% for issue in lang.issues %}
- [{{ issue.title }}]({{ issue.url }}) ({{ issue.comments }} comments)
{% endfor %}
{% endfor %}"""
        template_file.write_text(template_content)

        results = [
            {
                'language': 'Python',
                'issues': [
                    {
                        'title': 'Test Issue',
                        'url': 'https://example.com',
                        'comments': 5
                    }
                ]
            }
        ]

        today = "2024-03-01"
        
        # Create a temporary output file
        output_file = tmp_path / "README.md"
        
        # Only mock the write to README.md
        def mock_open_wrapper(original_open):
            def wrapped_open(*args, **kwargs):
                if args[0] == "README.md":
                    mock_file = MagicMock()
                    mock_file.write = MagicMock()
                    return mock_file
                return original_open(*args, **kwargs)
            return wrapped_open
        
        with patch('builtins.open', side_effect=mock_open_wrapper(open)) as mock_open:
            rendered = TemplateManager().render_template(results, str(template_dir), today)

            # Normalize whitespace for comparison
            def normalize_whitespace(text):
                # Remove empty lines and normalize remaining whitespace
                lines = [line.strip() for line in text.splitlines() if line.strip()]
                return '\n'.join(lines)

            rendered_normalized = normalize_whitespace(rendered)
            expected_normalized = normalize_whitespace("""# Good First Issues (2024-03-01)

## Python
- [Test Issue](https://example.com) (5 comments)""")

            assert rendered_normalized == expected_normalized
            
            # Verify the write to README.md
            write_calls = [call for call in mock_open.call_args_list if call[0][0] == "README.md"]
            assert len(write_calls) == 1
            assert write_calls[0][0][1] == "w+"

