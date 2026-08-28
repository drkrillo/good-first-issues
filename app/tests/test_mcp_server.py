import asyncio
import sys
from unittest.mock import patch

import pytest

from mcp.server.mcpserver import MCPServer

from app import mcp_server


CSV_HEADER = 'repo,language,title,url,comments,labels,created_at,updated_at\n'

CSV_ROWS = (
    'owner/alpha,Python,Fix the parser,https://github.com/owner/alpha/issues/1,'
    '0,"[\'good first issue\']",2026-01-01,2026-01-02\n'
    'other/gamma,Go,Add a retry,https://github.com/other/gamma/issues/3,'
    '2,"[\'good first issue\']",2026-01-05,2026-01-06\n'
)


@pytest.fixture
def dataset_env(tmp_path, monkeypatch):
    csv_file = tmp_path / 'issues.csv'
    csv_file.write_text(CSV_HEADER + CSV_ROWS, encoding='utf-8')
    monkeypatch.setenv('ISSUES_CSV', str(csv_file))
    return str(csv_file)


class TestLoadDataset:

    def test_load_dataset_reads_the_configured_file(self, dataset_env):
        result = mcp_server.load_dataset()

        assert len(result) == 2
        assert result[0]['repo'] == 'owner/alpha'


class TestSearchIssues:

    def test_search_issues_without_filters(self, dataset_env):
        result = mcp_server.search_issues()

        assert [i['comments'] for i in result] == [0, 2]

    def test_search_issues_with_filters(self, dataset_env):
        result = mcp_server.search_issues(
            language='Python',
            max_comments=0,
            label='good first issue',
            repo='owner',
            limit=5,
        )

        assert len(result) == 1
        assert result[0]['repo'] == 'owner/alpha'


class TestListLanguages:

    def test_list_languages_counts_every_language(self, dataset_env):
        result = mcp_server.list_languages()

        assert result == [
            {'language': 'Go', 'issues': 1},
            {'language': 'Python', 'issues': 1},
        ]


class TestListRepositories:

    def test_list_repositories_lists_them_all(self, dataset_env):
        result = mcp_server.list_repositories()

        assert len(result) == 2

    def test_list_repositories_narrowed_to_a_language(self, dataset_env):
        result = mcp_server.list_repositories(language='Go')

        assert result == [{'repo': 'other/gamma', 'issues': 1}]


class TestToolRegistration:

    def test_every_tool_is_registered(self):
        tools = asyncio.run(mcp_server.mcp.list_tools())

        names = {tool.name for tool in tools}
        assert names == {'search_issues', 'list_languages', 'list_repositories'}

    def test_every_tool_is_described_for_the_model(self):
        tools = asyncio.run(mcp_server.mcp.list_tools())

        assert all(tool.description for tool in tools)

    def test_search_issues_exposes_its_filters(self):
        tools = asyncio.run(mcp_server.mcp.list_tools())

        search = next(t for t in tools if t.name == 'search_issues')
        assert set(search.input_schema['properties']) == {
            'language', 'max_comments', 'label', 'repo', 'limit',
        }


def test_mcp_server_main_block(monkeypatch):
    """Test the __main__ block of mcp_server.py."""
    monkeypatch.setattr(sys, 'argv', ['mcp_server.py'])

    with patch.object(MCPServer, 'run') as mock_run:
        sys.modules.pop('app.mcp_server', None)
        import runpy
        runpy.run_module('app.mcp_server', run_name='__main__', alter_sys=True)

    mock_run.assert_called_once()
