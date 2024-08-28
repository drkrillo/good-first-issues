import os
from dotenv import load_dotenv


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
    "Authorization": f"Bearer  {ACCESS_TOKEN}"
}
