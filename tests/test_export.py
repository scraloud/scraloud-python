from scraloud import Client

def test_export_data():
    client = Client()
    data = {"key":"value"}
    assert client.export(data)