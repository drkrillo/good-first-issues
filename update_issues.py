import os
import datetime
from dotenv import load_dotenv

from github import Github, Auth

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
    'CNTK',
    'includeos',
    'xbmc',
    'monero-project',
    'StanGirard',
    'colinhacks',
    'godotengine',
]


def main():
    auth = Auth.Token(access_token)
    g = Github(auth=auth)

    results = []
    for username in usernames:
        try:
            user_data = g.get_user(username)

            for repo in user_data.get_repos():
                open_issues = repo.get_issues(
                    state='open',
                    labels=['good first issue'],
                    since=datetime.datetime(2019, 1, 1, 0, 0)
                )

                for issue in open_issues:
                    result = {
                        'repo': repo.full_name.split('/')[1],
                        'language': repo.language,
                        'title': issue.title,
                        'comments': str(issue.comments),
                        'url': issue.url.replace('api.','').replace('repos/',''),
                    }
                    results.append(result)

                
                print('done repo', repo.full_name)
        except Exception as e:
            print(e)

        results = sorted(results, key=lambda x: (x['language'], x['comments']))
        
        env = Environment(loader=FileSystemLoader('templates'))
        template = env.get_template('README.md.j2')

        today = str(datetime.datetime.today().strftime('%Y-%m-%d'))

        rendered_readme = template.render(results=results, today=today)

        with open("README.md", "w+") as f:
            f.write(rendered_readme)

if __name__ == "__main__":
    main()