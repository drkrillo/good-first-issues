# Using the Good First Issues Action

This Action fetches open issues labeled `good first issue` from the public repositories of specified GitHub users or organizations, and outputs the results as a CSV or JSON file.

## Quick Start

Add the following to `.github/workflows/good-first-issues.yml` in your repository:

```yaml
name: Good First Issues

on:
  schedule:
    - cron: '0 8 * * *' # runs daily at 08:00 UTC
  workflow_dispatch: # allows manual trigger

permissions:
  contents: read

jobs:
  fetch-issues:
    runs-on: ubuntu-latest
    steps:
      - uses: drkrillo/good-first-issues@main
        with:
          usernames: "pytorch,fastapi" # user/org to gather issues from
          github-token: ${{ secrets.GITHUB_TOKEN }}
```

This creates a `good_first_issues.csv` file as a workflow artifact with all discovered issues.

## Inputs

| Input | Required | Default | Description |
|---|---|---|---|
| `github-token` | Yes | — | GitHub token for API access. Use `${{ secrets.GITHUB_TOKEN }}` or a personal access token |
| `usernames` | No | `''` | Comma-separated list of GitHub usernames or organizations to scan |
| `output-format` | No | `csv` | Output format: `csv` or `json` |
| `output-path` | No | `<your_desired_file_name>.csv` | Path where the output file is written |

## Output Schema

Each issue in the output contains the following fields:

| Field | Description |
|---|---|
| `repo` | Repository full name (e.g. `pytorch/glow`) |
| `language` | Primary language of the repository |
| `title` | Issue title |
| `url` | Direct link to the issue on GitHub |
| `comments` | Number of comments on the issue |
| `labels` | Labels assigned to the issue |
| `state` | Issue state |

### CSV Example

```
repo,language,title,url,comments,labels,state
pytorch/glow,C++,Add layout propagation to NodeGen,https://github.com/pytorch/glow/issues/3834,0,['good first issue'],open
```

### JSON Example

```json
[
  {
    "repo": "pytorch/glow",
    "language": "C++",
    "title": "Add layout propagation to NodeGen",
    "url": "https://github.com/pytorch/glow/issues/3834",
    "comments": 0,
    "labels": ["good first issue"],
    "state": "open"
  }
]
```

## Workflow Examples

### Basic: Fetch and store as artifact

```yaml
name: Good First Issues

on:
  schedule:
    - cron: '0 8 * * *'
  workflow_dispatch:

permissions:
  contents: read

jobs:
  fetch:
    runs-on: ubuntu-latest
    steps:
      - uses: drkrillo/good-first-issues@main
        with:
          usernames: "pytorch,canonical"
          github-token: ${{ secrets.GITHUB_TOKEN }}

      - uses: actions/upload-artifact@v4
        with:
          name: good-first-issues
          path: good_first_issues.csv
```

### JSON output

```yaml
      - uses: drkrillo/good-first-issues@main
        with:
          usernames: "fastapi,django"
          github-token: ${{ secrets.GITHUB_TOKEN }}
          output-format: json
          output-path: issues.json
```

### Auto-update a README with the results

This is how this repository uses the action. The workflow fetches issues, renders them into a README using a Jinja2 template, and commits the result:

```yaml
name: Update Good First Issues

on:
  schedule:
    - cron: '15 20 * * *'
  push:
    branches: [main]
  workflow_dispatch:

permissions:
  contents: write

jobs:
  update:
    if: github.actor != 'github-actions[bot]'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: drkrillo/good-first-issues@main
        with:
          usernames: ${{ secrets.USERNAMES }}
          github-token: ${{ secrets.ACCESS_TOKEN }}
          output-path: good_first_issues.csv

      - name: Render README
        run: python -m app.render_readme --input good_first_issues.csv

      - name: Commit changes
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "41898282+github-actions[bot]@users.noreply.github.com"
          git add README.md good_first_issues.csv
          git diff --staged --quiet || git commit -m "chore: update good first issues"
          git push
```

## Authentication

The action requires a GitHub token to access the GitHub API.

- **`secrets.GITHUB_TOKEN`** — The default token provided by GitHub Actions. Works for public repositories. No setup needed.
- **Personal Access Token** — Required if you need higher rate limits or access to specific data. Create one with the `public_repo` scope under [Settings > Developer settings > Personal access tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens).

## Rate Limits

The GitHub API allows 5,000 authenticated requests per hour. Each username scanned requires a few API calls (one to list repositories, then one per repository to check for issues). This is more than enough for most use cases.

If you are scanning many usernames with hundreds of repositories, consider splitting the usernames across multiple workflow runs.
