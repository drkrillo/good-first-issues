# Testing

This project uses `pytest` and enforces **100% coverage** on every pull request.

## Running the tests

```bash
pip install -r requirements.txt
pytest --cov=app --cov-report=term-missing
```

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
