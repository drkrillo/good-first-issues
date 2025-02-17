import logging

import datetime
import time
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


today = str(datetime.datetime.today().strftime('%Y-%m-%d'))
template_path = get_template_path()

def main():
    """
    1- Gathers all issues associated with all public repos
    in the usernames list defined at the beginning of the scrit.
    2- Updates README.md file.
    """
    with requests.Session() as session:
        session.headers.update(HEADERS)
        logging.info("Gathering repositories...")
        repos = [RepoManager().extract_repos(user,  session) for user in USERNAMES]
        repos = Utils().create_list_from_lists(repos)
        logging.info(f"Extracted {len(repos)} public repositories.")

        logging.info(f"Gathering issues...")
        raw_issues = [IssueManager().extract_issues(repo, session) for repo in repos]
        raw_issues = Utils().create_list_from_lists(raw_issues)
        logging.info(f"Extracted {len(raw_issues)} issues.")

        logging.info("Normalizing data...")
        issues = [IssueManager().extract_issue_data(issue) for issue in raw_issues]
        logging.info(f"Normalized data.")
    
        formatted_response = TemplateManager.format_response(issues)
        TemplateManager.render_template(
            results=formatted_response,
            template_path=template_path,
            today=today,
        )

        logging.info(f"Rendered README file.")
        logging.info(f"Total repositories gathered: {len(repos)}")        
        logging.info(f"Total Issues gathered: {len(issues)}")

        
if __name__ == '__main__':

    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    logging.info(f"Script runtime: {end_time - start_time}")
