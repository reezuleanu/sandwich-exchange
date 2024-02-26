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
    """Test if it can connect to the db"""

    global db
    db = Database()
    assert db


# sandwich CRUD testing
def test_add_sandwich() -> None:
    """Test adding sandwich"""

    global sandwich_id
    rc, sandwich_id = db.add_sandwich(sandwich)
    assert rc


def test_get_sandwich_by_id() -> None:
    """Test getting sandwich by id"""

    query = db.get_sandwich_by_id(sandwich_id)
    assert query is not None


def test_update_sandwich_by_id() -> None:
    """Test modifying sandwich by id"""

    new_sandwich = sandwich
    new_sandwich.description = "This is no longer just a test sandwich"

    request = db.update_sandwich_by_id(sandwich_id, new_sandwich)
    assert request is True
    assert db.get_sandwich_by_id(sandwich_id) == new_sandwich


def test_query_database_by_name() -> None:
    """Test searching for sandwiches by name"""

    query = db.search_sandwiches_by_name(sandwich.name)
    assert query is not None

    response = {}

    for result in query:
        response[str(result["_id"])] = result["name"]

    assert str(sandwich_id) in response
    assert sandwich.name in response.values()


def test_delete_sandwich_by_id() -> None:
    """Test deleting sandwiches. This test should always be last"""

    request = db.delete_sandwich_by_id(sandwich_id)
    assert request is True
    assert db.get_sandwich_by_id(sandwich_id) is None
