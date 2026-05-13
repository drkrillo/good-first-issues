import logging

import datetime
import time
import argparse
import csv
import json
import requests

from jinja2 import Environment, FileSystemLoader

import app.core.config

from app.core.config import (
    HEADERS,
    USERNAMES,
    get_template_path,
    )
from app.core.api_handler import (
    RepoManager,
    IssueManager,
    TemplateManager,
    Utils,
)


def write_output(issues, output_file):
    """Write issues to a file in CSV or JSON format."""
    ext = output_file.lower().split('.')[-1]
    if ext == 'csv':
        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=['repo', 'language', 'title', 'url', 'comments', 'labels', 'state'])
            writer.writeheader()
            writer.writerows(issues)
    elif ext == 'json':
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(issues, f, indent=2)
    else:
        raise ValueError(f"Unsupported output format: .{ext} (use --output issues.csv or --output issues.json)")

def main(args):
    """
    1- Gathers all issues associated with all public repos
    in the usernames list defined at the beginning of the scrit.
    2- Updates README.md file.
    """
    with requests.Session() as session:
        session.headers.update(HEADERS)
        
        logging.info("Gathering repositories and language data...")
        repo_lang_map = {}
        for user in USERNAMES:
            user_repos = RepoManager().extract_repos(user, session)
            repo_lang_map.update(user_repos)
        logging.info(f"Extracted language data for {len(repo_lang_map)} repositories.")

        logging.info(f"Gathering issues using Search API...")
        all_raw_issues = []
        for user in USERNAMES:
            user_issues = IssueManager().extract_issues_by_user(user, session)
            # Map each issue to its repo's language
            for issue in user_issues:
                repo_url = issue['repository_url']
                lang = repo_lang_map.get(repo_url, "Other")
                all_raw_issues.append((lang, issue))
        
        logging.info(f"Extracted {len(all_raw_issues)} issues.")

        logging.info("Normalizing data...")
        issues = [IssueManager().extract_issue_data(issue) for issue in all_raw_issues]
        logging.info(f"Normalized data.")
        logging.info(f"First issues row: {issues[0]}")

        formatted_response = TemplateManager.format_response(issues)

        if args.output:
            write_output(formatted_response, args.output)
            logging.info(f"Wrote {len(issues)} issues to {args.output}")

        logging.info(f"Rendered README file.")
        logging.info(f"Total repositories gathered: {len(repo_lang_map)}")        
        logging.info(f"Total Issues gathered: {len(issues)}")

        
if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Find Good First Issues')
    parser.add_argument('--output', help='Output file path (e.g. issues.csv or issues.json)')
    args = parser.parse_args()

    start_time = time.perf_counter()
    main(args)
    end_time = time.perf_counter()
    logging.info(f"Script runtime: {end_time - start_time}")
