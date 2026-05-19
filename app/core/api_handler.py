import csv
import math 
import requests
from jinja2 import Environment, FileSystemLoader

from app.core.custom_exceptions import APIError
import app.core.config

import logging
from collections import defaultdict


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
        Takes a username, session and number of repos per page
        and returns a dictionary mapping repo URLs to their primary language.
        """
        repos_with_language = {}
        number_of_repos = RepoManager().extract_number_of_repos(user, session)
        number_of_pages = Utils().divide_and_round_up(number_of_repos)
        for page in range(1, number_of_pages + 1):
            user_url = f"https://api.github.com/users/{user}/repos?page={page}&per_page={repos_per_page}"
            resp_json = APIClient().make_request(user_url, session)
            try:
                for repo in resp_json:
                    lang = repo.get('language')
                    repos_with_language[repo['url']] = lang if lang else "Other"
            except TypeError as error:
                logging.error(error)
                raise

        return repos_with_language


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
            issue['labels'] = [l['name'] for l in raw_issue[1].get('labels', [])]
            issue['state'] = raw_issue[1].get('state', 'open')
        
            return issue
        except Exception as error:
            logging.error(error)
            raise


    @staticmethod
    def extract_issues_by_user(user, session, labels="good first issue"):
        """
        Uses GitHub Search API to find all issues with defined labels
        for a specific user/organization.
        """
        issues = []
        search_url = f"https://api.github.com/search/issues?q=user:{user}+label:\"{labels}\"+state:open+is:issue&per_page=100"
        
        resp_json = APIClient().make_request(search_url, session)
        try:
            # Search API returns total_count and items
            items = resp_json.get('items', [])
            # We don't have the language here, so we return raw issues
            # We will map the language in update_issues.py
            issues = items
        except Exception as error:
            logging.info(f"Error fetching issues for {user}: {error}")
            
        return issues


class TemplateManager:
    @staticmethod
    def format_response(issues: list) -> list:
        """
        Takes a list of issues, and returns them sorted by language and comments.
        """
        unique_languages = sorted(set([issue['language'] for issue in issues]))
        formatted_results = []

        for language in unique_languages:
            results = [issue for issue in issues if issue['language'] == language]
            sorted_results = sorted(results, key=lambda x: x['comments'])
            formatted_results.append(sorted_results)

        sorted_formatted_results = Utils.create_list_from_lists(formatted_results)
        return sorted_formatted_results

    @staticmethod
    def render_template(csv_path, template_path, today):
        """
        Takes a template, csv_path and today date
        and returns the rendered template.
        """
        results = []

        with open(csv_path, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)

            for row in reader:
                results.append({
                    'repo': row['repo'],
                    'language': row['language'],
                    'title': row['title'],
                    'url': row['url'],
                    'comments': row['comments'],
                })

        env = Environment(loader=FileSystemLoader(template_path))

        template = env.get_template('README.md.j2')
        rendered_readme = template.render(results=results, today=today)

        with open("README.md", "w+", encoding="utf-8") as f:
            f.write(rendered_readme)

        return rendered_readme

    @staticmethod
    def write_output(issues, output_file):
        """
        Write issues to a file in CSV or JSON format.
        """
        import json

        ext = output_file.lower().split('.')[-1]

        if ext == 'csv':
            with open(output_file, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(
                    f,
                    fieldnames=[
                        'repo',
                        'language',
                        'title',
                        'url',
                        'comments',
                        'labels',
                        'state'
                    ]
                )
                writer.writeheader()
                writer.writerows(issues)

        elif ext == 'json':
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(issues, f, indent=2)

        else:
            raise ValueError(
                f"Unsupported output format: .{ext} "
                f"(use --output issues.csv or --output issues.json)"
            )
    
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
        
