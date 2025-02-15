import math 
import requests
from jinja2 import Environment, FileSystemLoader

from app.core.custom_exceptions import APIError
import app.core.config


class RepoManager:
    @staticmethod
    def extract_number_of_repos(user, session):
        """
        Takes a username and aiohttp sesion and returns
        thetotal number of open repositories.
        """
        user_url = f"https://api.github.com/users/{user}"
        
        resp_json = APIClient().make_request(user_url, session)
        try:
            num_repos = resp_json['public_repos']
        except KeyError as error:
            logging.error(error)
            raise
        return num_repos

    @staticmethod
    def extract_repos(user, session, repos_per_page=100):
        """
        Takes a username, aiohttp sesion and number of repos pr page
        and returns list of lists of repositories. 
        """
        repos = []
        number_of_repos = RepoManager().extract_number_of_repos(user, session)
        number_of_pages = Utils().divide_and_round_up(number_of_repos)
        for page in range(1,number_of_pages+1):
            user_url = f"https://api.github.com/users/{user}/repos?page={page}&per_page={repos_per_page}"
            resp_json = APIClient().make_request(user_url, session)
            try: 
                repos += [x['url'] for x in resp_json]
            except TypeError as error:
                logging.error(error)
                raise

        return repos


class IssueManager:
    @staticmethod
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

    @staticmethod
    def extract_language(repo, session):
        """
        Takes the repo API endpoint and aiohttp session
        and returns the principal language of the repository.
        """
        resp_json = APIClient().make_request(repo, session)
        try:
            language = resp_json['language']
        except KeyError as error:
            logging.error(error)
            raise
            
        return language

    @staticmethod
    def extract_issues(repo, session, labels="good first issue"):
        """
        Takes the repo API endpoing and aiohttp session
        and returns issues  with defined labels and state.
        """
        issues = []
        language = IssueManager().extract_language(repo, session)
        issues_url = repo + f"/issues?labels={labels}"
        
        resp_json = APIClient().make_request(issues_url, session)
        try:
            cleaned_issues = [(language, issue) for issue in resp_json]
            issues += cleaned_issues
        except TypeError as error:
            logging.error(error)
            raise

        return issues


class TemplateManager:

    @staticmethod
    def format_response(issues: list) -> list:
        """
        Takes a list of dict issues, and returns it based on language.
        """
        unique_languages = set([issue['language'] for issue in issues])
        formatted_results = []	
        for language in unique_languages:
            results = [issue for issue in issues if issue['language'] == language]
            formatted_results.append({'language': language, 'issues': results})

        return results
    
    @staticmethod
    def render_template(results, template_path, today):
        """
        Takes a jinja2 environment, template, results and today date
        and returns the rendered template.
        """
        env = Environment(loader=FileSystemLoader(template_path))
        
        template = env.get_template('README.md.j2')
        rendered_readme = template.render(results=results, today=today)
        
        with open("README.md", "w+") as f:
            f.write(rendered_readme)
        
        return rendered_readme
    
class Utils:
    @staticmethod
    def divide_and_round_up(num: int,  denom: int=100):
        """
        Takes two numbers and returns the first biggest int.
        """
        total = num / denom
        total_round_up = math.ceil(total)
        return total_round_up
    
    @staticmethod
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
    
class APIClient:
    @staticmethod
    def make_request(url, session):
        try:
            resp = session.get(url)
            resp.raise_for_status()
            return resp.json()
        except requests.exceptions.HTTPError as error:
            raise APIError(resp.status_code, resp.text) from error
        except Exception as error:
            logging.error(f'Another error occurred: {error}')
            raise
        