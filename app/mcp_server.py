from mcp.server.mcpserver import MCPServer

from app.core.config import get_dataset_path
from app.core.dataset import DatasetManager


mcp = MCPServer(
    name='good-first-issues',
    instructions=(
        'Search the good first issues dataset this repository builds. '
        'The data is whatever the pipeline last wrote locally, so it follows '
        'the usernames this checkout is configured for. Call list_languages '
        'before search_issues to see which languages are actually present.'
    ),
)


def load_dataset():
    """
    Returns the issues held in the dataset the pipeline last wrote.
    """
    return DatasetManager.load_issues(get_dataset_path())


@mcp.tool()
def search_issues(
    language: str | None = None,
    max_comments: int | None = None,
    label: str | None = None,
    repo: str | None = None,
    limit: int = 20,
    max_age_days: int | None = None
) -> list[dict]:
    """
    Search the good first issues dataset, least discussed issues first.

    Set max_comments to 0 for issues nobody has commented on yet, which are
    the ones least likely to be claimed already. The language must match one
    reported by list_languages. The repo filter matches on a substring of
    owner/name, so "django" finds every Django repository at once.

    Set max_age_days to only return issues updated within that many days.
    An issue labeled good first issue that nobody has touched in years is
    not really available, and this dataset has plenty of those — use this
    filter when the goal is a currently active issue, not just any match.
    """
    return DatasetManager.filter_issues(
        load_dataset(),
        language=language,
        max_comments=max_comments,
        label=label,
        repo=repo,
        limit=limit,
        max_age_days=max_age_days
    )


@mcp.tool()
def list_languages() -> list[dict]:
    """
    List the languages present in the dataset with their issue count,
    most issues first. Use it to pick a valid language for search_issues.
    """
    return DatasetManager.count_by_language(load_dataset())


@mcp.tool()
def list_repositories(language: str | None = None) -> list[dict]:
    """
    List the repositories present in the dataset with their issue count,
    most issues first, optionally narrowed to a single language.
    """
    return DatasetManager.count_by_repo(load_dataset(), language=language)


if __name__ == '__main__':

    mcp.run()
