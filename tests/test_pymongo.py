from server.database import Database
from server.models import Sandwich, Price_history
from datetime import datetime


sandwich = Sandwich(
    name="Test Sandwich",
    description="this is just a test sandwich",
    price_history=Price_history.generate_history(datetime(2020, 1, 1), datetime.now()),
    volume=5000,
    on_sale=4000,
)


def test_database_connection() -> None:
    global db
    db = Database()


# sandwich CRUD testing
def test_add_sandwich() -> None:
    global sandwich_id
    rc, sandwich_id = db.add_sandwich(sandwich)
    assert rc


def test_get_sandwich_by_id() -> None:
    query = db.get_sandwich_by_id(sandwich_id)
    assert query is not None


def test_update_sandwich_by_id() -> None:
    new_sandwich = sandwich
    new_sandwich.description = "This is no longer just a test sandwich"

    request = db.update_sandwich_by_id(sandwich_id, new_sandwich)
    assert request is True
    assert db.get_sandwich_by_id(sandwich_id) == new_sandwich


def test_query_database_by_name() -> None:
    query = db.search_sandwiches_by_name(sandwich.name)
    assert query[0] is not None

    assert query[0]["_id"] == sandwich_id
    assert query[0]["name"] == sandwich.name


def test_get_sandwich_by_name() -> None:
    assert True


def test_get_sandwich_id_by_name() -> None:
    assert True


def test_delete_sandwich_by_id() -> None:
    request = db.delete_sandwich_by_id(sandwich_id)
    assert request is True
    assert db.get_sandwich_by_id(sandwich_id) is None
