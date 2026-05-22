# Local Setup

## Prerequisites

- Python 3.11+
- A GitHub account with a personal access token

## 1. Clone the repository

```bash
git clone https://github.com/drkrillo/good-first-issues.git
cd good-first-issues
```

---

# Create a Virtual Environment

Using a virtual environment helps keep project dependencies isolated.

## Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

## Windows

```bash
python -m venv venv
venv\\Scripts\\activate
```

---

# Install Dependencies

Install the required Python packages using:

```bash
pip install -r requirements.txt
```

## 4. Create the `.env` file

Create a file named `.env` in the project root with the following variables:

```
ACCESS_TOKEN=<YOUR_GITHUB_TOKEN>
USERNAMES=<OWNER1>,<OWNER2>,<OWNER3>
```

- **`ACCESS_TOKEN`** — A GitHub personal access token (see below).
- **`USERNAMES`** — Comma-separated list of GitHub usernames or organizations whose repositories will be scanned for good first issues.

## 5. Obtain a GitHub personal access token

1. Go to **Settings > Developer settings > Personal access tokens > Tokens (classic)** in your GitHub account.
2. Click **Generate new token (classic)**.
3. Give it a descriptive name (e.g. `good-first-issues`).
4. Select the **`public_repo`** scope — this is the only scope required.
5. Click **Generate token** and copy it into your `.env` file.

For more details, see the [official GitHub documentation](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens).

## 6. Run the script

```bash
python -m app.update_issues --output good_first_issues.csv
```

This fetches all good first issues from the configured usernames and writes them to the specified output file (`.csv` or `.json`).

To render the README from the generated data:

```bash
python -m app.render_readme --input good_first_issues.csv
```
