import os

import requests


def export(data):
    item_url = os.environ.get("SCRALOUD_ITEM_URL")
    spider_id = os.environ.get("SCRALOUD_SPIDER_ID")
    params = {"spider_id": spider_id}
    response = requests.post(item_url, params=params, json=data)
    return response