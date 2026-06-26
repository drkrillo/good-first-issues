# Testing Documentation

## Overview
This document describes the testing strategy and coverage for the Good First Issues project. We use pytest as our testing framework and aim to maintain 100% test coverage across all components.

## Test Coverage

⚠️ Note: As of the latest test run, several tests are failing due to
recent changes in `IssueManager` (the `extract_language` and
`extract_issues` methods were removed/consolidated into
`extract_issue_data`). The table below does not reflect current
passing status.

Run the following to see current status:
```bash
python -m pytest app/tests/ -v --cov=app

## Test Structure
gti
### 1. Core Components Tests (`test_api_handler.py`)

#### RepoManager Tests
- `test_extract_number_of_repos`: Tests successful repository count extraction
- `test_extract_repos`: Tests repository list extraction with pagination
- `test_extract_number_of_repos_error`: Tests error handling for missing data
- `test_extract_repos_error`: Tests error handling for invalid responses

#### IssueManager Tests
- `test_extract_issue_data`: Tests issue data extraction and formatting
- `test_extract_language`: Tests repository language detection
- `test_extract_issues`: Tests issue extraction with labels
- Error handling tests for each method

#### Utils Tests
- `test_utils_divide_and_round_up`: Tests pagination calculation
- `test_utils_create_list_from_lists`: Tests list flattening functionality

#### APIClient Tests
- `test_apiclient_make_request_success`: Tests successful API requests
- `test_apiclient_make_request_error`: Tests HTTP error handling
- `test_apiclient_make_request_general_error`: Tests general error handling

#### TemplateManager Tests
- `test_format_response`: Tests issue grouping by language
- `test_render_template`: Tests template rendering with Jinja2

### 2. Main Script Tests (`test_update_issues.py`)

- `test_main_flow`: Tests the complete workflow
- `test_main_with_no_repos`: Tests behavior with no repositories
- `test_main_with_no_issues`: Tests behavior with no issues
- `test_main_script_execution`: Tests script runtime measurement

## Running Tests

To run the test suite:
```bash
python -m pytest app/tests/ -v --cov=app
```

For detailed coverage report:
```bash
python -m pytest app/tests/ -v --cov=app --cov-report term-missing
```

## Test Fixtures

Key fixtures (defined in `conftest.py`):
- `mock_session`: Mocks requests.Session for API calls
- `mock_env_vars`: Sets up environment variables for testing

## Error Testing Strategy

We test various error scenarios:
1. API errors (404, rate limits, etc.)
2. Missing or malformed data
3. File system errors
4. Environment configuration errors

## Maintenance Guidelines

When adding new features:
1. Maintain 100% coverage for new code
2. Add tests for both success and error cases
3. Mock external dependencies
4. Test edge cases and boundary conditions

When modifying existing code:
1. Run the test suite to ensure no regressions
2. Update tests if behavior changes
3. Add new test cases for bug fixes

## Common Testing Patterns

1. API Mocking:
```python
@patch('app.core.api_handler.APIClient')
def test_function(self, mock_api_client):
    mock_api_instance = MagicMock()
    mock_api_client.return_value = mock_api_instance
    # Test implementation
```

2. File Operations:
```python
def test_file_operations(self, tmp_path):
    # Use tmp_path for temporary file creation
    temp_file = tmp_path / "test.txt"
    # Test implementation
```

3. Error Handling:
```python
with pytest.raises(ExpectedError):
    # Code that should raise ExpectedError
``` 