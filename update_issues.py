import logging

import datetime
import time
import requests 

from jinja2 import Environment, FileSystemLoader

from config import ACCESS_TOKEN, USERNAMES, HEADERS
from api_handler import APIHandler

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)

today = str(datetime.datetime.today().strftime('%Y-%m-%d'))
 
 
def main():
    """
    1- Gathers all issues associated with all public repos
    in the usernames list defined at the beginning of the scrit.
    2- Updates README.md file.
    """
    with requests.Session() as session:
        session.headers.update(HEADERS)
        logging.info("Gathering repositories...")
        api_handler = APIHandler()
        repos = [api_handler.extract_repos(user,  session) for user in USERNAMES]
        repos = api_handler.create_list_from_lists(repos)
        logging.info(f"Extracted {len(repos)} public repositories.")

        logging.info(f"Gathering issues...")
        raw_issues = [api_handler.extract_issues(repo, session) for repo in repos]
        raw_issues = api_handler.reate_list_from_lists(raw_issues)
        logging.info(f"Extracted {len(raw_issues)} issues.")

        logging.info("Normalizing data...")
        issues = [api_handler.extract_issue_data(issue) for issue in raw_issues]
        issues = sorted(issues, key=lambda x: (x['language'] or '', x['comments'] or 0))
        logging.info(f"Normalized data.")

        env = Environment(loader=FileSystemLoader('templates'))
        template = env.get_template('README.md.j2')
        rendered_readme = template.render(results=issues, today=today)
        
        with open("README.md", "w+") as f:
            f.write(rendered_readme)
        
        logging.info(f"Rendered README file.")
        logging.info(f"Total repositories gathered: {len(repos)}")        
        logging.info(f"Total Issues gathered: {len(issues)}")

        
if __name__ == '__main__':

    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    logging.info(f"Script runtine: {end_time - start_time}")
