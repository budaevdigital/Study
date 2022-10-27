from datetime import datetime

import requests


def task(task_id):
    response = requests.get("https://python.org")
    response_html = response.text
    print(response_html[:15])
