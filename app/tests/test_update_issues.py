import pytest
from unittest.mock import patch, MagicMock
import datetime
import time

from app.update_issues import main
from app.core.api_handler import RepoManager, IssueManager, TemplateManager, Utils


@pytest.fixture
def mock_session():
    with patch('requests.Session') as mock:
        session = MagicMock()
        mock.return_value.__enter__.return_value = session
        yield session


def test_main_flow(mock_session, mock_env_vars):
    # Mock the repository data
    repos = [
        "https://api.github.com/repos/owner/repo1",
        "https://api.github.com/repos/owner/repo2"
    ]
    
    # Mock the raw issues data
    raw_issues = [
        ("Python", {
            "repository_url": "https://api.github.com/repos/owner/repo1",
            "title": "Test Issue 1",
            "html_url": "https://github.com/owner/repo1/issues/1",
            "comments": 5
        }),
        ("JavaScript", {
            "repository_url": "https://api.github.com/repos/owner/repo2",
            "title": "Test Issue 2",
            "html_url": "https://github.com/owner/repo2/issues/2",
            "comments": 3
        })
    ]
    
    # Mock the processed issues
    processed_issues = [
        {
            "repo": "owner/repo1",
            "language": "Python",
            "title": "Test Issue 1",
            "url": "https://github.com/owner/repo1/issues/1",
            "comments": 5
        },
        {
            "repo": "owner/repo2",
            "language": "JavaScript",
            "title": "Test Issue 2",
            "url": "https://github.com/owner/repo2/issues/2",
            "comments": 3
        }
    ]
    
    # Mock the formatted response
    formatted_response = [
        {
            'language': 'JavaScript',
            'issues': [{
                "repo": "owner/repo2",
                "language": "JavaScript",
                "title": "Test Issue 2",
                "url": "https://github.com/owner/repo2/issues/2",
                "comments": 3
            }]
        },
        {
            'language': 'Python',
            'issues': [{
                "repo": "owner/repo1",
                "language": "Python",
                "title": "Test Issue 1",
                "url": "https://github.com/owner/repo1/issues/1",
                "comments": 5
            }]
        }
    ]
    
    # Mock all the necessary components
    with patch.object(RepoManager, 'extract_repos', return_value=repos), \
         patch.object(Utils, 'create_list_from_lists', side_effect=[repos, raw_issues]), \
         patch.object(IssueManager, 'extract_issues', return_value=raw_issues), \
         patch.object(IssueManager, 'extract_issue_data', side_effect=lambda x: {
             "repo": x[1]["repository_url"].split('repos/')[1],
             "language": x[0],
             "title": x[1]["title"],
             "url": x[1]["html_url"],
             "comments": x[1]["comments"]
         }), \
         patch.object(TemplateManager, 'format_response', return_value=formatted_response) as mock_format, \
         patch.object(TemplateManager, 'render_template') as mock_render:
        
        # Run the main function
        main()
        
        # Verify the session was configured correctly
        mock_session.headers.update.assert_called_once()
        
        # Verify format_response was called with processed issues
        mock_format.assert_called_once()
        format_args = mock_format.call_args[0][0]
        assert len(format_args) == 2
        assert any(issue["repo"] == "owner/repo1" for issue in format_args)
        assert any(issue["repo"] == "owner/repo2" for issue in format_args)
        
        # Verify render_template was called with formatted response
        mock_render.assert_called_once()
        render_kwargs = mock_render.call_args[1]
        assert render_kwargs["results"] == formatted_response
        assert "template_path" in render_kwargs
        assert "today" in render_kwargs
        assert render_kwargs["today"] == datetime.datetime.today().strftime('%Y-%m-%d')


def test_main_with_no_repos(mock_session, mock_env_vars):
    with patch.object(RepoManager, 'extract_repos', return_value=[]), \
         patch.object(IssueManager, 'extract_issues') as mock_extract_issues, \
         patch.object(TemplateManager, 'format_response') as mock_format, \
         patch.object(TemplateManager, 'render_template') as mock_render:
        
        # Run the main function
        main()
        
        # Verify no issues were extracted since there were no repos
        mock_extract_issues.assert_not_called()
        
        # Verify template was still rendered (but with empty results)
        mock_format.assert_called_once_with([])
        mock_render.assert_called_once()


def test_main_with_no_issues(mock_session, mock_env_vars):
    repos = ["https://api.github.com/repos/owner/repo1"]
    
    with patch.object(RepoManager, 'extract_repos', return_value=repos), \
         patch.object(IssueManager, 'extract_issues', return_value=[]), \
         patch.object(TemplateManager, 'format_response') as mock_format, \
         patch.object(TemplateManager, 'render_template') as mock_render:
        
        # Run the main function
        main()
        
        # Verify template was rendered with empty results
        mock_format.assert_called_once_with([])
        mock_render.assert_called_once()


def test_main_script_execution(mock_session, mock_env_vars, monkeypatch):
    # Mock time.perf_counter to return predictable values
    counter = 0
    def mock_perf_counter():
        nonlocal counter
        counter += 1
        return counter
    monkeypatch.setattr('time.perf_counter', mock_perf_counter)
    
    # Mock logging to capture the output
    mock_logger = MagicMock()
    monkeypatch.setattr('logging.info', mock_logger)
    
    # Import and run the script's __main__ block
    import runpy
    runpy.run_module('app.update_issues', run_name='__main__')
    
    # Verify logging was called with runtime
    mock_logger.assert_called_with('Script runtime: 1') 