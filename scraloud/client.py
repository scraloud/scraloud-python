import os

import requests


def export(data):
    item_url = os.environ.get("SCRALOUD_ITEM_URL")
    scraper_id = os.environ.get("SCRALOUD_SCRAPER_ID")
    params = {"scraper_id": scraper_id}
    response = requests.post(item_url, params=params, json=data)
    return response
