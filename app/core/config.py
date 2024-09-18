import os
from dotenv import load_dotenv
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)


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


def get_template_path():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_dir, 'app', 'templates')