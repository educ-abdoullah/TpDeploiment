import requests

URL = "http://127.0.0.1:8080"

def test_health():
    response = requests.get(f"{URL}/health")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_addition():
    response = requests.get(f"{URL}/addition/5/5")

    assert response.status_code == 200
    assert response.json()["result"] == 10