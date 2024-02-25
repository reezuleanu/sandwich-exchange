import requests
import sys
from datetime import datetime

# sys.path.append("../")
from server.models import Sandwich, Price_history
from server.database import Database

api_url = "http://127.0.0.1:2727"
db = Database()

sandwich = Sandwich(
    name="Api Test Sandwich",
    price_history=Price_history.generate_history(datetime(2020, 1, 1), datetime.now()),
)


def test_post_sandwich() -> None:
    response = requests.post(f"{api_url}/sandwich/", json=sandwich.model_dump())
    assert response.status_code == 200


def test_search_sandwiches():
    response = requests.get(f"{api_url}/sandwiches/search/{sandwich.name}")

    assert response.status_code == 200
    assert type(response.json()) is dict
    assert sandwich.name in response.json().values()

    # set id for rest of tests
    global id
    id = list(response.json().keys())[0]


def test_get_sandwich_by_id() -> None:
    response = requests.get(f"{api_url}/sandwich/{id}")
    assert response.status_code == 200
    result = Sandwich(**response.json())
    assert result.name == sandwich.name

    # check if pydantic converts the iso strings properly
    assert type(result.price_history.x[0]) is datetime


def test_update_sandwich() -> None:
    # modify sandwich
    sandwich_modified = sandwich
    sandwich_modified.name = "Modified Api Test Sandwich"
    sandwich_modified.description = "This is a modified api test sandwich"

    # put request
    response = requests.put(
        f"{api_url}/sandwich/{id}", json=sandwich_modified.model_dump()
    )

    assert response.status_code == 200

    # check database details

    response = requests.get(f"{api_url}/sandwich/{id}")
    db_sandwich = Sandwich(**response.json())

    # check some values
    assert db_sandwich.name == sandwich_modified.name
    assert db_sandwich.description == sandwich_modified.description
    assert db_sandwich.price == sandwich.price


def test_delete_sandwich() -> None:
    response = requests.delete(f"{api_url}/sandwich/{id}")
    assert response.status_code == 200

    # check the sandwich is actually gone
    assert requests.get(f"{api_url}/sandwich/{id}").status_code == 404
