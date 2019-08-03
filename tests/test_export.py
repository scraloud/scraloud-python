import os

from scraloud import export

def test_export_data():
    os.environ.setdefault("SCRALOUD_ITEM_URL", "https://httpbin.org/post")
    data = {"key":"value"}
    assert export(data)