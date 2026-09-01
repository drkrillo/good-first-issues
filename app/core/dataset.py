import ast
import csv

from app.core.custom_exceptions import DatasetError
from datetime import date, timedelta

import logging
from collections import defaultdict


class DatasetManager:
    @staticmethod
    def parse_labels(raw_labels):
        """
        Takes the labels column as written to the CSV and returns
        the label names as a list. Reads both the Python list repr and the
        semicolon separated text, so a dataset written by either version of
        the pipeline can be queried.
        """
        if not raw_labels:
            return []

        if raw_labels.lstrip().startswith('['):
            try:
                return list(ast.literal_eval(raw_labels))
            except (ValueError, SyntaxError) as error:
                logging.error(error)
                return []

        return [label.strip() for label in raw_labels.split(';') if label.strip()]

    @staticmethod
    def load_issues(csv_path):
        """
        Takes the path of the dataset written by the pipeline and returns
        its issues, with the comment count as an int and the labels as a list.
        """
        issues = []
        try:
            with open(csv_path, newline='', encoding='utf-8') as f:
                reader = csv.DictReader(f)

                for row in reader:
                    issues.append({
                        'repo': row['repo'],
                        'language': row['language'],
                        'title': row['title'],
                        'url': row['url'],
                        'comments': int(row['comments']),
                        'labels': DatasetManager.parse_labels(row.get('labels', '')),
                        'created_at': row.get('created_at', ''),
                        'updated_at': row.get('updated_at', ''),
                    })
        except FileNotFoundError as error:
            logging.error(error)
            raise DatasetError(csv_path) from error

        return issues

    @staticmethod
    def filter_issues(issues, language=None, max_comments=None,
                      label=None, repo=None, limit=20, max_age_days: int | None = None):
        """
        Takes a list of issues and the filters to apply, and returns the
        matching ones sorted by comment count, least discussed first.

        max_age_days filters on the updated_at, inclusive of boundary. 
        Issues with no updated_at are excluded, since recency can't be verified for them.   
        """
        results = issues       
        if language:
            results = [i for i in results
                       if i['language'].lower() == language.lower()]
        if max_comments is not None:
            results = [i for i in results if i['comments'] <= max_comments]
        if label:
            results = [i for i in results
                       if any(label.lower() == l.lower() for l in i['labels'])]
        if repo:
            results = [i for i in results if repo.lower() in i['repo'].lower()]
        if max_age_days is not None:
            cutoff = date.today() - timedelta(days=max_age_days)
            filtered = []
            for i in results:
                if not i['updated_at']:
                    continue  
                if date.fromisoformat(i['updated_at']) >= cutoff:
                    filtered.append(i)
            results = filtered

        sorted_results = sorted(results, key=lambda i: i['comments'])
        return sorted_results[:limit]

    @staticmethod
    def count_by_language(issues):
        """
        Takes a list of issues and returns the languages present in it,
        with their issue count, most issues first.
        """
        counts = defaultdict(int)
        for issue in issues:
            counts[issue['language']] += 1

        return [
            {'language': language, 'issues': total}
            for language, total in sorted(counts.items(),
                                          key=lambda item: (-item[1], item[0]))
        ]

    @staticmethod
    def count_by_repo(issues, language=None):
        """
        Takes a list of issues and an optional language, and returns the
        repositories present, with their issue count, most issues first.
        """
        counts = defaultdict(int)
        for issue in issues:
            if language and issue['language'].lower() != language.lower():
                continue
            counts[issue['repo']] += 1

        return [
            {'repo': repo, 'issues': total}
            for repo, total in sorted(counts.items(),
                                      key=lambda item: (-item[1], item[0]))
        ]
