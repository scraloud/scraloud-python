import os

import requests


def export(data):
    item_url = os.environ.get("SCRALOUD_ITEM_URL")
    spider_id = os.environ.get("SCRALOUD_SPIDER_ID")
    url = item_url + "?spider_id=" + spider_id
    response = requests.post(url, json=data)
    return response