from fastapi import APIRouter, HTTPException
import sys
from datetime import datetime

# sys.path.append("../")
from ..models import Sandwich, Price_history
from ..database import Database

sandwiches_r = APIRouter()
db = Database()


@sandwiches_r.get("/sandwiches/{sandwich_id}")
def get_sandwich_by_id(sandwich_id: str) -> Sandwich:
    """Api call to get sandwich data by id

    Args:
        sandwich_id (str): sandwich id in the database

    Raises:
        HTTPException: 404 error

    Returns:
        Sandwich: sandwich data
    """

    query = db.get_sandwich_by_id(sandwich_id)
    if query is None:
        raise HTTPException(404)

    return query


@sandwiches_r.post("/sandwiches/")
def add_sandwich(sandwich: Sandwich) -> dict:
    """Api call that creates sandwich"""

    # check if it already has a price history. if not, generate it
    if sandwich.price_history is None:
        sandwich.price_history = Price_history.generate_history(
            datetime(2020, 1, 1), datetime.now()
        )

    rc, _ = db.add_sandwich(sandwich)

    if rc is False:
        raise HTTPException(500)
    return {"response": "sandwich added successfully"}


@sandwiches_r.put("/sandwiches/{sandwich_id}")
def update_sandwich(sandwich_id: str, sandwich: Sandwich) -> dict:

    query = db.get_sandwich_by_id(sandwich_id)
    if query is None:
        raise HTTPException(404)

    rc = db.update_sandwich_by_id(sandwich_id, sandwich)
    if rc is False:
        raise HTTPException(500)
    return {"response": "sandwich updated successfully"}


@sandwiches_r.delete("/sandwiches/{sandwich_id}")
def delete_sandwich(sandwich_id: str) -> dict:
    """Api call that deletes sandwich by id"""

    rc = db.delete_sandwich_by_id(sandwich_id)

    if rc is False:
        raise HTTPException(504)

    return {"response": "sandwich deleted successfully"}


@sandwiches_r.get("/sandwiches/search/")
def find_sandwich_by_name(search: str) -> dict:
    """Api call that queries the database for sandwiches by name"""

    # todo make a name index
    # todo make searches case insensitive and non exact
    # todo make it sort by price
    query = db.search_sandwiches_by_name(search)
    if query is None:
        raise HTTPException(404)

    # turn cursor into a dictionary
    # the key is the id
    # the value is the name
    response = {}
    for sandwich in query:
        response[str(sandwich["_id"])] = sandwich["name"]

    return response
