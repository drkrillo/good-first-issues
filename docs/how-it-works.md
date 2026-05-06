## How it Works

This project automates the discovery of good first-issues using GitHub API:

* **Smart Discovery**: `RepoManager` identifies all public repositories from the usernames defined in your `.env` file.
* **Issue Filtering**: `IssueManager` searches those repositories for issues labeled with `good first issue`.
* **Language Matchmaking**: It identifies the primary language of each repository to help you find tasks in your area of expertise.
* **Automated Rendering**: Uses **Jinja2** templates and the `TemplateManager` to render the gathered data into this README file.
* **Daily Updates**: A GitHub Action runs the `update_issues.py` script daily to ensure the list is always updated.