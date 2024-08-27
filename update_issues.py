import os
from dotenv import load_dotenv
import random
import logging

import datetime
import time

import math 

import asyncio, aiohttp

from jinja2 import Environment, FileSystemLoader

from exception_handler import APIError

load_dotenv()
ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')
USERNAMES = [
    "pandas-dev",
    'django',
    'flask',
    'fastapi',
    'ansible',
    'tensorflow',
    'pytorch',
    'opencv',
    'zeromicro',
    'includeos',
    'xbmc',
    'monero-project',
    'StanGirard',
    'colinhacks',
    'godotengine',
]

HEADERS = {
    "Authorization": f" Bearer  {ACCESS_TOKEN}"
}

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)

today = str(datetime.datetime.today().strftime('%Y-%m-%d'))


def divide_and_round_up(num: int,  denom: int=100):
    """
    Takes two numbers and returns the first biggest int.
    """
    total = num / denom
    total_round_up = math.ceil(total)
    return total_round_up

def create_list_from_lists(target: list):
    """
    Takes a list of lists and 
    returns a coninuous list with aall elements.
    """
    list_of_lists = []
    for element in target:
        if element != None:
            for e in element:
                list_of_lists.append(e)
    return list_of_lists

def extract_issue_data(raw_issue: tuple):
    """
    Takes an issue (language, issue dict)
    and returns a depurated dict withissue data.
    """
    issue = {}
    try:
        issue['repo'] = raw_issue[1]['repository_url'].split('repos/')[1]
        issue['language'] = raw_issue[0]
        issue['title'] = raw_issue[1]['title']
        issue['url'] = raw_issue[1]['html_url']
        issue['comments'] = raw_issue[1]['comments']
    
        return issue
    except Exception as error:
        logging.error(error)
        raise

async def extract_language(repo, session):
    """
    Takes the repo API endpoint and aiohttp session
    and returns the principal language of the repository.
    """
    async with session.get(repo) as resp:
        resp_json = await resp.json()
        
        if resp.status != 200:
            raise APIError(resp.status, resp_json['message'])
    
        try:
            language = resp_json['language']
        except KeyError as error:
            logging.error(error)
            raise
        
        return language

async def extract_issues(repo, session, labels="good first issue"):
    """
    Takes the repo API endpoing and aiohttp session
    and returns issues  with defined labels and state.
    """
    issues = []
    language = await extract_language(repo, session)
    issues_url = repo + f"/issues?labels={labels}"

    async with session.get(issues_url) as resp:
        resp_json = await resp.json()
        
        if resp.status != 200:
            raise APIError(resp.status, resp_json['message'])

        try:
            cleaned_issues = [(language, issue) for issue in resp_json]
            issues += cleaned_issues
        except TypeError as error:
            logging.error(error)
            raise

        return issues

async def extract_number_of_repos(user, session):
    """
    Takes a username and aiohttp sesion and returns
    thetotal number of open repositories.
    """
    import ipdb; ipdb.set_trace()
    user_url = f"https://api.github.com/users/{user}"

    async with session.get(user_url) as resp:
        resp_json = await resp.json()
        
        if resp.status != 200:
            raise APIError(resp.status, resp_json['message'])

        try:
            num_repos = resp_json['public_repos']
        except KeyError as error:
            logging.error(error)
            raise

        return num_repos

async def extract_repos(user, session, repos_per_page=100):
    """
    Takes a username, aiohttp sesion and number of repos pr page
    and returns list of lists of repositories. 
    """
    repos = []
    number_of_repos = await extract_number_of_repos(user, session)
    number_of_pages = divide_and_round_up(number_of_repos)
    for page in range(1,number_of_pages+1):
        user_url = f"https://api.github.com/users/{user}/repos?page={page}&per_page={repos_per_page}"
        
        async with session.get(user_url) as resp:
            resp_json = await resp.json()

            if resp.status != 200:
                raise APIError(resp.status, resp_json['message'])
            
            try: 
                repos += [x['url'] for x in resp_json]
            except TypeError as error:
                logging.error(error)
                raise

            return repos
    
async def main():
    """
    1- Gathers all issues associated with all public repos
    in the usernames list defined at the beginning of the scrit.
    2- Updates README.md file.
    """
    async with aiohttp.ClientSession(headers=HEADERS) as session:
        logging.info("Gathering repositories...")
        repos = [extract_repos(user,  session) for user in USERNAMES]
        repos = await  asyncio.gather(*repos)
        repos = create_list_from_lists(repos)
        logging.info(f"Extracted {len(repos)} public repositories.")

        logging.info(f"Gathering issues...")
        raw_issues = [extract_issues(repo, session) for repo in repos]
        raw_issues = await asyncio.gather(*raw_issues)
        raw_issues = create_list_from_lists(raw_issues)
        logging.info(f"Extracted {len(raw_issues)} issues.")

        logging.info("Normalizing data...")
        issues = [extract_issue_data(issue) for issue in raw_issues]
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
    asyncio.run(main())
    end_time = time.perf_counter()
    logging.info(f"Script runtine: {end_time - start_time}")
