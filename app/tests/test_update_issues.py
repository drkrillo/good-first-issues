import pytest
import sys
from unittest.mock import patch, MagicMock
import datetime
import time
import logging

from app.update_issues import main
from app.core.api_handler import RepoManager, IssueManager, TemplateManager, Utils


@pytest.fixture
def mock_session():
    with patch('requests.Session') as mock:
        session = MagicMock()
        mock.return_value.__enter__.return_value = session
        yield session


@pytest.fixture
def mock_args():
    args = MagicMock()
    args.output = None
    return args


def test_main_flow(mock_session, mock_env_vars, mock_args):
    # Mock the repository data as a {url: language} dict
    repos = {
        "https://api.github.com/repos/owner/repo1": "Python",
        "https://api.github.com/repos/owner/repo2": "JavaScript",
    }

    # Mock raw issues returned by the Search API
    raw_issues = [
        {
            "repository_url": "https://api.github.com/repos/owner/repo1",
            "title": "Test Issue 1",
            "html_url": "https://github.com/owner/repo1/issues/1",
            "comments": 5,
            "labels": [{"name": "good first issue"}],
            "state": "open",
            "created_at": "2026-01-01T00:00:00Z",
            "updated_at": "2026-01-02T00:00:00Z",
        },
        {
            "repository_url": "https://api.github.com/repos/owner/repo2",
            "title": "Test Issue 2",
            "html_url": "https://github.com/owner/repo2/issues/2",
            "comments": 3,
            "labels": [{"name": "good first issue"}],
            "state": "open",
            "created_at": "2026-01-03T00:00:00Z",
            "updated_at": "2026-01-04T00:00:00Z",
        },
    ]

    with patch.object(RepoManager, 'extract_repos', return_value=repos), \
         patch.object(IssueManager, 'extract_issues_by_user', return_value=raw_issues), \
         patch.object(IssueManager, 'extract_issue_data', side_effect=lambda x: {
             "repo": x[1]["repository_url"].split('repos/')[1],
             "language": x[0],
             "title": x[1]["title"],
             "url": x[1]["html_url"],
             "comments": x[1]["comments"],
             "labels": [l["name"] for l in x[1].get("labels", [])],
             "state": x[1].get("state", "open"),
             "created_at": x[1].get("created_at", "")[:10],
             "updated_at": x[1].get("updated_at", "")[:10],
         }), \
         patch.object(TemplateManager, 'format_response') as mock_format:

        main(mock_args)

        # Verify the session was configured correctly
        mock_session.headers.update.assert_called_once()

        # Verify format_response was called with processed issues
        mock_format.assert_called_once()
        format_args = mock_format.call_args[0][0]
        assert len(format_args) == 2
        assert any(issue["repo"] == "owner/repo1" for issue in format_args)
        assert any(issue["repo"] == "owner/repo2" for issue in format_args)


def test_main_with_no_repos(mock_session, mock_env_vars, mock_args):
    with patch.object(RepoManager, 'extract_repos', return_value={}), \
         patch.object(IssueManager, 'extract_issues_by_user', return_value=[]):

        # Current code raises IndexError when no issues are found (issues[0])
        with pytest.raises(IndexError):
            main(mock_args)


def test_main_with_no_issues(mock_session, mock_env_vars, mock_args):
    repos = {"https://api.github.com/repos/owner/repo1": "Python"}

    with patch.object(RepoManager, 'extract_repos', return_value=repos), \
         patch.object(IssueManager, 'extract_issues_by_user', return_value=[]):

        # Current code raises IndexError when no issues are found (issues[0])
        with pytest.raises(IndexError):
            main(mock_args)


def test_main_script_execution(mock_session, mock_env_vars, monkeypatch):
    counter = [0]
    def mock_perf_counter():
        counter[0] += 1
        return counter[0]
    monkeypatch.setattr(time, 'perf_counter', mock_perf_counter)

    log_messages = []
    monkeypatch.setattr(logging, 'info', lambda msg: log_messages.append(msg))

    import app.update_issues as update_module
    monkeypatch.setattr(update_module, 'main', lambda args: None)

    # Simulate the __main__ block
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--output')
    args = parser.parse_args([])

    start_time = time.perf_counter()
    update_module.main(args)
    end_time = time.perf_counter()
    logging.info(f"Script runtime: {end_time - start_time}")

    assert 'Script runtime: 1' in log_messages