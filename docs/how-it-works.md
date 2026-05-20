## How it Works

This project automates the discovery of good first-issues using GitHub API:

* **Smart Discovery**: `RepoManager` identifies all public repositories from the usernames defined in your `.env` file.
* **Issue Filtering**: `IssueManager` searches those repositories for issues labeled with `good first issue`.
* **Language Matchmaking**: It identifies the primary language of each repository to help you find tasks in your area of expertise.
* **Automated Rendering**: Uses **Jinja2** templates and the `TemplateManager` to render the gathered data into this README file.
* **Daily Updates**: A GitHub Action runs the `update_issues.py` script daily to ensure the list is always updated.

# Running the Project Locally

## Clone the Repository

```bash
git clone https://github.com/drkrillo/good-first-issues.git
cd good-first-issues
```

---

## Create a Virtual Environment

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### Windows

```bash
python -m venv venv
venv\\Scripts\\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create a `.env` file and configure the required GitHub token and settings.

Example:

```env
GITHUB_TOKEN=your_token_here
```

---

## Run the Project

```bash
python app/update_issues.py
```
