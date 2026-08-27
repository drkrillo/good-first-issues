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
USERNAMES = os.environ.get('USERNAMES', '').split(',')
USERNAMES = [user.strip() for user in USERNAMES if user.strip()]

HEADERS = {
    "Authorization": f"Bearer  {ACCESS_TOKEN}"
}

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def get_template_path():
    return os.path.join(BASE_DIR, 'templates')


def get_dataset_path():
    """
    Returns the path to the issues dataset, taken from the ISSUES_CSV
    environment variable and falling back to the file the pipeline
    writes at the repository root.
    """
    default_path = os.path.join(os.path.dirname(BASE_DIR), 'good_first_issues.csv')
    return os.environ.get('ISSUES_CSV', default_path)
