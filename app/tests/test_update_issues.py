from types import SimpleNamespace
from unittest.mock import MagicMock, patch

from app.core.api_handler import IssueManager, RepoManager, TemplateManager
from app.update_issues import main


def test_main_collects_issues_and_writes_output():
    repo_url = "https://api.github.com/repos/owner/repo1"
    raw_issue = {
        "repository_url": repo_url,
        "title": "Test Issue",
        "html_url": "https://github.com/owner/repo1/issues/1",
        "comments": 5,
        "labels": [{"name": "good first issue"}],
        "state": "open",
    }

    args = SimpleNamespace(output="issues.csv")

    with patch("requests.Session") as mock_session_class, \
         patch("app.update_issues.USERNAMES", ["owner"]), \
         patch.object(RepoManager, "extract_repos", return_value={repo_url: "Python"}), \
         patch.object(IssueManager, "extract_issues_by_user", return_value=[raw_issue]), \
         patch.object(TemplateManager, "format_response", side_effect=lambda issues: issues) as mock_format, \
         patch.object(TemplateManager, "write_output") as mock_write:

        session = MagicMock()
        mock_session_class.return_value.__enter__.return_value = session

        main(args)

        session.headers.update.assert_called_once()
        formatted_issues = mock_format.call_args.args[0]

        assert formatted_issues == [
            {
                "repo": "owner/repo1",
                "language": "Python",
                "title": "Test Issue",
                "url": "https://github.com/owner/repo1/issues/1",
                "comments": 5,
                "labels": ["good first issue"],
                "state": "open",
            }
        ]
        mock_write.assert_called_once_with(formatted_issues, "issues.csv")


def test_main_uses_other_language_when_repo_language_missing():
    raw_issue = {
        "repository_url": "https://api.github.com/repos/owner/missing",
        "title": "Unknown Language Issue",
        "html_url": "https://github.com/owner/missing/issues/1",
        "comments": 0,
    }

    args = SimpleNamespace(output="issues.csv")

    with patch("requests.Session") as mock_session_class, \
         patch("app.update_issues.USERNAMES", ["owner"]), \
         patch.object(RepoManager, "extract_repos", return_value={}), \
         patch.object(IssueManager, "extract_issues_by_user", return_value=[raw_issue]), \
         patch.object(TemplateManager, "format_response", side_effect=lambda issues: issues) as mock_format, \
         patch.object(TemplateManager, "write_output") as mock_write:

        session = MagicMock()
        mock_session_class.return_value.__enter__.return_value = session

        main(args)

        formatted_issues = mock_format.call_args.args[0]
        assert formatted_issues[0]["language"] == "Other"
        mock_write.assert_called_once_with(formatted_issues, "issues.csv")
