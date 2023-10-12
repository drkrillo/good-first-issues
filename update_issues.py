import os
import datetime
from dotenv import load_dotenv
import time

import math 

import asyncio, aiohttp

from jinja2 import Environment, FileSystemLoader


load_dotenv()
access_token = os.environ.get('ACCESS_TOKEN')

usernames = [
    "pandas-dev",
    'django',
    'flask',
    'fastapi',
    'ansible',
    'tensorflow'
    'pytorch',
    'opencv',
    'includeos',
    'xbmc',
    'monero-project',
    'StanGirard',
    'colinhacks',
    'godotengine',
]

gathered_users = []

headers = {
    "Authorization": f" Bearer  {access_token}"
}

def define_number_of_pages(number_of_repos, total_repos_per_page=100):
    number_of_pages = number_of_repos / total_repos_per_page
    number_of_pages = math.ceil(number_of_pages)
    return number_of_pages

def create_list_from_lists(target_list):
    list_of_lists = []
    for element in target_list:
        if len(element) > 0:
            for e in element:
                list_of_lists.append(e)
    return list_of_lists

def extract_issue_data(raw_issue):
    issue = {}
    issue['repo'] = raw_issue[1]['repository_url'].split('repos/')[1]
    issue['language'] = raw_issue[0]
    issue['title'] = raw_issue[1]['title']
    issue['url'] = raw_issue[1]['html_url']
    issue['comments'] = raw_issue[1]['comments']
    return issue

async def extract_language(repo, session):
    async with session.get(repo)as resp:
        repo = await resp.json()
        language = repo['language']
    return language

async def extract_issues(repo, session):
    issues = []
    language = await extract_language(repo, session)
    issues_url = repo + "/issues?labels=good first issue"
    async with session.get(issues_url) as resp:
        resp = await resp.json()
        if len(resp) > 0:
            resp = [(language, r) for r in resp]
            issues += resp
    return issues

async def extract_number_of_repos(user, session):
    user_url = f"https://api.github.com/users/{user}"
    async with session.get(user_url) as resp:
        resp = await resp.json()
    try:
        num_repos = resp['public_repos']
    except:
        num_repos = 100
    return num_repos

async def extract_repos(user, session, repos_per_page=100):
    repos = []
    number_of_repos = await extract_number_of_repos(user, session)
    number_of_pages = define_number_of_pages(number_of_repos)
    
    for page in range(1,number_of_pages+1):
        user_url = f"https://api.github.com/users/{user}/repos?page={page}&per_page={repos_per_page}"

        async with session.get(user_url) as resp:
            user = await resp.json()
            if type(user) == list:
                repos += [x['url'] for x in user]
        return repos

async def main():
    async with aiohttp.ClientSession(headers=headers) as session:
        
        repos = [extract_repos(user,  session) for user in usernames]
        repos = await  asyncio.gather(*repos)
        repos= create_list_from_lists(repos)
        
        issues = [extract_issues(repo, session) for repo in repos]
        issues = await asyncio.gather(*issues)
        issues = create_list_from_lists(issues)

        issues = [extract_issue_data(issue) for issue in issues]
        issues = sorted(issues, key=lambda x: (x['language'], x['comments']))
        
        print(f"Total Issues gathered: {len(issues)}")
        env = Environment(loader=FileSystemLoader('templates'))
        template = env.get_template('README.md.j2')
        today = str(datetime.datetime.today().strftime('%Y-%m-%d'))
        rendered_readme = template.render(results=issues, today=today)
        
        with open("README.md", "w+") as f:
            f.write(rendered_readme)

if __name__ == '__main__':
    start_time = time.perf_counter() 
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
    end_time = time.perf_counter()
    print(f"Script runtine: {end_time - start_time}")