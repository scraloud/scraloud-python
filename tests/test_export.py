import os

from scraloud import export

def test_export_data():
    os.environ.setdefault("SCRALOUD_ITEM_URL", "https://httpbin.org/post")
    os.environ.setdefault("SCRALOUD_SCRAPER_ID", "1")
    data = {"key":"value"}
    resp = export(data)
    assert resp.status_code == 200
    assert resp.json()["data"] == '{"key": "value"}'
    assert resp.json()["args"]["scraper_id"] == "1"