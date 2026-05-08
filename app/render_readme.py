import argparse
from datetime import datetime

from app.core.api_handler import TemplateManager
from app.core.config import get_template_path


today = str(datetime.datetime.today().strftime('%Y-%m-%d'))
template_path = get_template_path()

if "__main__" == __name__:

    parser = argparse.ArgumentParser(description='Find Good First Issues')
    parser.add_argument('--output', help='Output file path (e.g. issues.csv or issues.json)')
    args = parser.parse_args()
    
    TemplateManager.render_template(
    csv_path=args.output,
    template_path=template_path,
    today=today,
)