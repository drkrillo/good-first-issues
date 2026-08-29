import os

import pytest

from datetime import date, timedelta

from app.core.config import get_dataset_path
from app.core.dataset import DatasetManager
from app.core.custom_exceptions import DatasetError


CSV_HEADER = 'repo,language,title,url,comments,labels,created_at,updated_at\n'

CSV_ROWS = (
    'owner/alpha,Python,Fix the parser,https://github.com/owner/alpha/issues/1,'
    '0,"[\'good first issue\', \'bug\']",2026-01-01,2026-01-02\n'
    'owner/beta,Python,Document the API,https://github.com/owner/beta/issues/2,'
    '5,"[\'good first issue\', \'docs\']",2026-01-03,2026-01-04\n'
    'other/gamma,Go,Add a retry,https://github.com/other/gamma/issues/3,'
    '2,"[\'good first issue\']",2026-01-05,2026-01-06\n'
)


@pytest.fixture
def dataset_file(tmp_path):
    csv_file = tmp_path / 'issues.csv'
    csv_file.write_text(CSV_HEADER + CSV_ROWS, encoding='utf-8')
    return str(csv_file)


@pytest.fixture
def issues(dataset_file):
    return DatasetManager.load_issues(dataset_file)


class TestParseLabels:

    def test_parse_labels_returns_the_names(self):
        result = DatasetManager.parse_labels("['good first issue', 'bug']")

        assert result == ['good first issue', 'bug']

    def test_parse_labels_reads_the_semicolon_form(self):
        result = DatasetManager.parse_labels('bug; docs')

        assert result == ['bug', 'docs']

    def test_parse_labels_on_a_single_label(self):
        assert DatasetManager.parse_labels('bug') == ['bug']

    def test_parse_labels_drops_empty_segments(self):
        assert DatasetManager.parse_labels('bug;; docs;') == ['bug', 'docs']

    def test_parse_labels_on_empty_value(self):
        assert DatasetManager.parse_labels('') == []

    def test_parse_labels_on_an_unreadable_repr(self):
        assert DatasetManager.parse_labels("['unclosed") == []


class TestLoadIssues:

    def test_load_issues_normalizes_the_rows(self, dataset_file):
        result = DatasetManager.load_issues(dataset_file)

        assert len(result) == 3
        assert result[0]['repo'] == 'owner/alpha'
        assert result[0]['language'] == 'Python'
        assert result[0]['comments'] == 0
        assert result[0]['labels'] == ['good first issue', 'bug']
        assert result[0]['created_at'] == '2026-01-01'
        assert result[0]['updated_at'] == '2026-01-02'

    def test_load_issues_without_a_dataset(self, tmp_path):
        missing = str(tmp_path / 'nothing.csv')

        with pytest.raises(DatasetError):
            DatasetManager.load_issues(missing)


class TestFilterIssues:

    def test_filter_issues_without_filters_sorts_by_comments(self, issues):
        result = DatasetManager.filter_issues(issues)

        assert [i['comments'] for i in result] == [0, 2, 5]

    def test_filter_issues_by_language(self, issues):
        result = DatasetManager.filter_issues(issues, language='python')

        assert len(result) == 2
        assert all(i['language'] == 'Python' for i in result)

    def test_filter_issues_by_max_comments(self, issues):
        result = DatasetManager.filter_issues(issues, max_comments=0)

        assert len(result) == 1
        assert result[0]['repo'] == 'owner/alpha'

    def test_filter_issues_by_label(self, issues):
        result = DatasetManager.filter_issues(issues, label='DOCS')

        assert len(result) == 1
        assert result[0]['repo'] == 'owner/beta'

    def test_filter_issues_by_label_on_the_semicolon_form(self, tmp_path):
        csv_file = tmp_path / 'semicolon.csv'
        csv_file.write_text(
            CSV_HEADER
            + 'owner/delta,Rust,Tidy the docs,'
              'https://github.com/owner/delta/issues/4,1,bug; docs,'
              '2026-01-07,2026-01-08\n',
            encoding='utf-8',
        )

        issues = DatasetManager.load_issues(str(csv_file))
        result = DatasetManager.filter_issues(issues, label='docs')

        assert len(result) == 1
        assert result[0]['labels'] == ['bug', 'docs']

    def test_filter_issues_by_repo_substring(self, issues):
        result = DatasetManager.filter_issues(issues, repo='owner/')

        assert len(result) == 2

    def test_filter_issues_honours_the_limit(self, issues):
        result = DatasetManager.filter_issues(issues, limit=1)

        assert len(result) == 1

    def test_filter_issues_boundary_case(self, tmp_path):
        updated_at = date.today().isoformat()
        created_at = (date.today() - timedelta(days=200)).isoformat()
        csv_content = (
            CSV_HEADER +
            f'owner/recent,Python,Fresh issue,https://github.com/owner/recent/issues/1,'
            f'0,"[\'good first issue\']",{updated_at},{updated_at}\n'
            f'owner/old,Python,Stale issue,https://github.com/owner/old/issues/2,'
            f'0,"[\'good first issue\']",{created_at},{created_at}\n'
        )
        csv_file = tmp_path / 'issues.csv'
        csv_file.write_text(csv_content, encoding='utf-8')
        issues = DatasetManager.load_issues(str(csv_file))
        result = DatasetManager.filter_issues(issues, max_age_days=0)
        assert len(result) == 1
        assert result[0]['repo'] == 'owner/recent'

    def test_filter_issues_empty_updated_at(self, tmp_path):
            updated_at = date.today().isoformat()
            created_at = (date.today() - timedelta(days=200)).isoformat()
            csv_content = (
                CSV_HEADER +
                f'owner/empty_updated_at,Python,Fresh issue,https://github.com/owner/recent/issues/1,'
                f'0,"[\'good first issue\']",{created_at},\n'
                f'owner/with_updated_at,Python,Stale issue,https://github.com/owner/old/issues/2,'
                f'0,"[\'good first issue\']",{created_at},{updated_at}\n'
            )
            csv_file = tmp_path / 'issues.csv'
            csv_file.write_text(csv_content, encoding='utf-8')
            issues = DatasetManager.load_issues(str(csv_file))
            result = DatasetManager.filter_issues(issues, max_age_days=0)
            assert len(result) == 1
            assert result[0]['repo'] == 'owner/with_updated_at'

    def test_filter_issues_without_max_age_days(self, issues):
        result = DatasetManager.filter_issues(issues, max_age_days=None)
        assert len(result) == len(issues)


class TestCountByLanguage:

    def test_count_by_language_orders_by_count(self, issues):
        result = DatasetManager.count_by_language(issues)

        assert result == [
            {'language': 'Python', 'issues': 2},
            {'language': 'Go', 'issues': 1},
        ]


class TestCountByRepo:

    def test_count_by_repo_lists_every_repository(self, issues):
        result = DatasetManager.count_by_repo(issues)

        assert result == [
            {'repo': 'other/gamma', 'issues': 1},
            {'repo': 'owner/alpha', 'issues': 1},
            {'repo': 'owner/beta', 'issues': 1},
        ]

    def test_count_by_repo_narrowed_to_a_language(self, issues):
        result = DatasetManager.count_by_repo(issues, language='go')

        assert result == [{'repo': 'other/gamma', 'issues': 1}]


class TestDatasetError:

    def test_dataset_error_names_the_path(self):
        error = DatasetError('/tmp/missing.csv')

        assert '/tmp/missing.csv' in str(error)


class TestConfig:

    def test_get_dataset_path_defaults_to_the_repository_root(self, monkeypatch):
        monkeypatch.delenv('ISSUES_CSV', raising=False)

        result = get_dataset_path()

        assert os.path.basename(result) == 'good_first_issues.csv'

    def test_get_dataset_path_honours_the_environment(self, monkeypatch):
        monkeypatch.setenv('ISSUES_CSV', '/tmp/custom.csv')

        assert get_dataset_path() == '/tmp/custom.csv'
