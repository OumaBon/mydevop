from conftest import client


def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Home" in response.data
