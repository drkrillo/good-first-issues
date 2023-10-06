from pprint import pprint
from github import Github, Auth
from inspect import getmembers
import datetime
from jinja2 import Environment, FileSystemLoader

results = []
access_token = "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"

auth = Auth.Token(access_token)
g = Github(auth=auth)

usernames = [
    "pandas-dev",
    'django',
    'flask',
    'fastapi',
    'ansible',
    'tensorflow'
    'pytorch',
    'opencv',
]
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

headers = "| Repo | Language | Title | Comments |\n"
headers_line = "| --- | --- | --- | --- |\n"

whole_table = headers + headers_line
for result in results:
  generated_string = f"| {result['repo']} | {result['language']} | [{result['title']}]({result['url']}) | {result['comments']} |\n"
  whole_table += generated_string

env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('README.md.j2')

rendered_readme = template.render(results=results)


with open("README.md", "w+") as f:
    f.write(rendered_readme)