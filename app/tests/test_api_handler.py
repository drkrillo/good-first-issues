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
            [{"url": "https://api.github.com/repos/owner/repo1", "language": "Python"},
             {"url": "https://api.github.com/repos/owner/repo2", "language": "JavaScript"}],
            [{"url": "https://api.github.com/repos/owner/repo3", "language": None}]
        ]

        result = RepoManager().extract_repos('test_user', mock_api_instance)

        assert len(result) == 3
        assert result == {
            "https://api.github.com/repos/owner/repo1": "Python",
            "https://api.github.com/repos/owner/repo2": "JavaScript",
            "https://api.github.com/repos/owner/repo3": "Other",
        }
        
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
                "comments": 5,
                "labels": [{"name": "good first issue"}],
                "state": "open",
                "created_at": "2026-05-20T12:34:56Z",
                "updated_at": "2026-07-29T08:00:00Z",
            }
        )

        result = IssueManager().extract_issue_data(raw_issue)

        assert result == {
            "repo": "owner/repo",
            "language": "Python",
            "title": "Test Issue",
            "url": "https://github.com/owner/repo/issues/1",
            "comments": 5,
            "labels": ["good first issue"],
            "created_at": "2026-05-20",
            "updated_at": "2026-07-29",
        }

    @patch('app.core.api_handler.APIClient')
    def test_extract_issues_by_user(self, mock_api_client):
        mock_api_instance = MagicMock()
        mock_api_client.return_value = mock_api_instance

        mock_api_instance.make_request.return_value = {
            "items": [
                {
                    "title": "Test Issue",
                    "html_url": "https://github.com/owner/repo/issues/1",
                    "repository_url": "https://api.github.com/repos/owner/repo",
                    "comments": 5,
                }
            ]
        }

        result = IssueManager().extract_issues_by_user("test_user", mock_api_instance)

        assert len(result) == 1
        assert result[0]["title"] == "Test Issue"
        mock_api_instance.make_request.assert_called_once()

    @patch('app.core.api_handler.APIClient')
    def test_extract_issues_by_user_error(self, mock_api_client):
        mock_api_instance = MagicMock()
        mock_api_client.return_value = mock_api_instance
        # Return a non-dict so .get() raises AttributeError
        mock_api_instance.make_request.return_value = None

        result = IssueManager().extract_issues_by_user("test_user", mock_api_instance)

        # The except block catches the error and returns empty list
        assert result == []

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

        # Returns a flat list sorted by language, then by comments
        assert len(result) == 3

        # JavaScript comes first alphabetically
        assert result[0]['language'] == 'JavaScript'
        assert result[0]['title'] == 'Issue 3'

        # Python issues sorted by comments (ascending)
        assert result[1]['language'] == 'Python'
        assert result[1]['comments'] == 2
        assert result[2]['language'] == 'Python'
        assert result[2]['comments'] == 5

    def test_render_template(self, tmp_path):
        # Create a temporary template file
        template_dir = tmp_path / "templates"
        template_dir.mkdir()
        template_file = template_dir / "README.md.j2"
        template_content = """# Good First Issues ({{ today }})

{% for result in results -%}
| {{ result.repo }} | {{ result.language }} | [{{ result.title }}]({{ result.url }}) | {{ result.comments }} |
{% endfor %}"""
        template_file.write_text(template_content)

        # Create a temporary CSV file
        csv_file = tmp_path / "issues.csv"
        csv_file.write_text(
            "repo,language,title,url,comments,created_at,updated_at\n"
            "owner/repo,Python,Test Issue,https://example.com,5,2024-01-01,2024-01-02\n"
        )

        today = "2024-03-01"

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
            rendered = TemplateManager().render_template(
                str(csv_file), str(template_dir), today
            )

            assert "Good First Issues (2024-03-01)" in rendered
            assert "owner/repo" in rendered
            assert "Python" in rendered
            assert "Test Issue" in rendered

            # Verify the write to README.md
            write_calls = [call for call in mock_open.call_args_list if call[0][0] == "README.md"]
            assert len(write_calls) == 1
            assert write_calls[0][0][1] == "w+"

    def test_write_output_csv(self, tmp_path):
        issues = [
            {
                'repo': 'owner/repo',
                'language': 'Python',
                'title': 'Issue 1',
                'url': 'https://example.com',
                'comments': 5,
                'labels': ['good first issue'],
                'created_at': '2024-01-01',
                'updated_at': '2024-01-02',
            }
        ]
        output_file = str(tmp_path / "output.csv")

        TemplateManager.write_output(issues, output_file)

        with open(output_file) as f:
            content = f.read()
        assert "owner/repo" in content
        assert "Python" in content

    def test_write_output_json(self, tmp_path):
        import json
        issues = [
            {
                'repo': 'owner/repo',
                'language': 'Python',
                'title': 'Issue 1',
                'url': 'https://example.com',
                'comments': 5,
            }
        ]
        output_file = str(tmp_path / "output.json")

        TemplateManager.write_output(issues, output_file)

        with open(output_file) as f:
            data = json.load(f)
        assert len(data) == 1
        assert data[0]['repo'] == 'owner/repo'

    def test_write_output_invalid_format(self, tmp_path):
        output_file = str(tmp_path / "output.txt")

        with pytest.raises(ValueError, match="Unsupported output format"):
            TemplateManager.write_output([], output_file)


class TestConfig:
    def test_get_template_path(self):
        from app.core.config import get_template_path
        result = get_template_path()
        assert "templates" in result

