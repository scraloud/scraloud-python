import os

import requests


def export(data):
    response = requests.post(os.environ.get("SCRALOUD_ITEM_URL"), json=data)
    return response.status_code == 200