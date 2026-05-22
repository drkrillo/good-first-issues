# Local Setup

This guide explains how to run the project locally for development or testing.

---

# Clone the Repository

First, clone the repository and move into the project directory.

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

---

# Configure Environment Variables

Create a `.env` file in the root of the project.

The `.env` file stores configuration values such as your GitHub token and the usernames or organizations to scan.

Example:

```env
GITHUB_TOKEN=your_token_here
USERNAMES=python,github,microsoft
```

`USERNAMES` defines which GitHub users or organizations will be scanned for issues.

---

# Run the Project

Generate issues in JSON format:

```bash
python app.update_issues.py --output issues.json
```

Generate issues in CSV format:

```bash
python app.update_issues.py --output issues.csv
```

---

# Output Files

The generated output file will contain the collected issues in the selected format.
