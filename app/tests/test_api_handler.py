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
        assert result == {
            "https://api.github.com/repos/owner/repo1": "Other",
            "https://api.github.com/repos/owner/repo2": "Other",
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
                "comments": 5
            }
        )
        
        result = IssueManager().extract_issue_data(raw_issue)
        
        assert result == {
            "repo": "owner/repo",
            "language": "Python",
            "title": "Test Issue",
            "url": "https://github.com/owner/repo/issues/1",
            "comments": 5,
            "labels": [],
            "state": "open",
        }

    @patch('app.core.api_handler.APIClient')
    def test_extract_issues_by_user(self, mock_api_client):
        mock_api_instance = MagicMock()
        mock_api_client.return_value = mock_api_instance
        mock_api_instance.make_request.return_value = {
            "items": [
                {
                    "repository_url": "https://api.github.com/repos/owner/repo",
                    "title": "Test Issue",
                    "html_url": "https://github.com/owner/repo/issues/1",
                    "comments": 5,
                }
            ]
        }

        result = IssueManager().extract_issues_by_user("test_user", mock_api_instance)

        assert len(result) == 1
        assert result[0]["title"] == "Test Issue"
        mock_api_instance.make_request.assert_called_once_with(
            'https://api.github.com/search/issues?q=user:test_user+label:"good first issue"+state:open+is:issue&per_page=100',
            mock_api_instance,
        )

    @patch('app.core.api_handler.APIClient')
    def test_extract_issues_by_user_empty_response(self, mock_api_client):
        mock_api_instance = MagicMock()
        mock_api_client.return_value = mock_api_instance
        mock_api_instance.make_request.return_value = {}

        result = IssueManager().extract_issues_by_user("test_user", mock_api_instance)

        assert result == []

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

        assert len(result) == 3
        assert [issue["language"] for issue in result] == ["JavaScript", "Python", "Python"]
        assert [issue["comments"] for issue in result] == [3, 2, 5]

    def test_render_template(self, tmp_path, monkeypatch):
        template_dir = tmp_path / "templates"
        template_dir.mkdir()

        template_file = template_dir / "README.md.j2"
        template_file.write_text(
            "{% for issue in results %}{{ issue.repo }}|{{ issue.language }}|{{ issue.title }}|{{ issue.url }}|{{ issue.comments }}\n{% endfor %}",
            encoding="utf-8",
        )

        csv_path = tmp_path / "issues.csv"
        csv_path.write_text(
            "repo,language,title,url,comments,labels,state\n"
            "owner/repo,Python,A|B,https://example.com,2,[],open\n",
            encoding="utf-8",
        )

        monkeypatch.chdir(tmp_path)

        rendered = TemplateManager().render_template(
            str(csv_path),
            str(template_dir),
            "2026-07-07",
        )

        assert "owner/repo|Python|A\\|B|https://example.com|2" in rendered
        assert (tmp_path / "README.md").read_text(encoding="utf-8") == rendered
