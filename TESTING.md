# Testing

This project uses `pytest` and enforces **100% coverage** on every pull request.

## Running the tests

```bash
pip install -r requirements.txt -r requirements-mcp.txt
pytest --cov=app --cov-report=term-missing
```

The MCP dependency lives in `requirements-mcp.txt` so the GitHub Action does
not have to install it, but the test suite covers `app/mcp_server.py`, so you
need both files to reach 100%.

To check the coverage gate the same way CI does:

```bash
coverage report --fail-under=100
```

## Continuous integration

`.github/workflows/tests.yml` runs on every pull request and on every push to
`main`, against Python 3.12 and 3.13.

It fails if:

- any test fails, or
- total coverage drops below 100%

**A pull request that lowers coverage will not pass CI.** If you add code, add
the tests that cover it in the same PR.

## Test layout

### `app/tests/test_api_handler.py`

Grouped in classes, one per component:

| Class | Covers |
|---|---|
| `TestRepoManager` | repository count and listing, with pagination and error paths |
| `TestIssueManager` | issue extraction and field parsing, plus their error paths |
| `TestUtils` | pagination maths and list flattening |
| `TestAPIClient` | HTTP requests, HTTP errors and unexpected errors |
| `TestAPIError` | the custom exception's string representation |
| `TestTemplateManager` | grouping by language, Jinja2 rendering, and CSV/JSON output |
| `TestConfig` | template path resolution |

### `app/tests/test_dataset.py`

Grouped in classes, one per component:

| Class | Covers |
|---|---|
| `TestParseLabels` | reading the labels column, including unreadable values |
| `TestLoadIssues` | dataset normalization, and the missing dataset error path |
| `TestFilterIssues` | every filter, the sort order and the limit |
| `TestCountByLanguage` | language counts and their ordering |
| `TestCountByRepo` | repository counts, with and without a language |
| `TestDatasetError` | the custom exception's string representation |
| `TestConfig` | dataset path resolution, default and `ISSUES_CSV` |

### `app/tests/test_mcp_server.py`

The MCP tools, each against a dataset written to `tmp_path` and pointed at with
`ISSUES_CSV`: `search_issues` with and without filters, `list_languages`,
`list_repositories`, that the three tools are registered and described for the
model, and the `__main__` block.

### `app/tests/test_update_issues.py`

The end-to-end flow of the script: the normal run, the empty cases (no repos, no
issues), the `--output` flag, and the `__main__` blocks of `update_issues` and
`render_readme`.

## Fixtures

In `app/tests/conftest.py`:

- `mock_session` — a mock of `requests.Session`
- `mock_env_vars` — patches `HEADERS` and `USERNAMES` in `app.update_issues`

Local to `test_update_issues.py`:

- `mock_args` — a mock of the parsed CLI arguments

## Writing tests

Mock the API client rather than making real requests:

```python
@patch('app.core.api_handler.APIClient')
def test_something(self, mock_api_client):
    mock_api_instance = MagicMock()
    mock_api_client.return_value = mock_api_instance
```

Use `tmp_path` for anything that touches the filesystem, and cover the error
path as well as the happy one — most classes here have both.
