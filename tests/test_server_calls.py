import requests
import sys

sys.path.append("../server")
from server.models import Sandwich

api_url = "http://127.0.0.1:2727"


def test_get_sandwich() -> None:
    sandwich = "subway footlong"
    response = requests.get(f"{api_url}/sandwiches/{sandwich}")

    assert response.status_code == 200
    assert response.json()["name"] == sandwich
    assert response.json()["price"] == 9999
