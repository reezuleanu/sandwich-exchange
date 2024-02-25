from fastapi import APIRouter, HTTPException
import sys
from datetime import datetime

# sys.path.append("../")
from ..models import Sandwich, Price_history
from ..database import Database

sandwiches_r = APIRouter()
db = Database()


@sandwiches_r.get("/sandwich/{sandwich_id}")
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


@sandwiches_r.post("/sandwich")
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


@sandwiches_r.put("/sandwich/{sandwich_id}")
def update_sandwich(sandwich_id: str, sandwich: Sandwich) -> dict:

    query = db.get_sandwich_by_id(sandwich_id)
    if query is None:
        raise HTTPException(404)

    rc = db.update_sandwich_by_id(sandwich_id, sandwich)
    if rc is False:
        raise HTTPException(500)
    return {"response": "sandwich updated successfully"}


@sandwiches_r.delete("/sandwich/{sandwich_id}")
def delete_sandwich(sandwich_id: str) -> dict:
    """Api call that deletes sandwich by id"""

    rc = db.delete_sandwich_by_id(sandwich_id)

    if rc is False:
        raise HTTPException(504)

    return {"response": "sandwich deleted successfully"}


@sandwiches_r.get("/sandwiches/search/{search}")
def find_sandwich_by_name(search: str) -> dict:
    """Api call that queries the database for sandwiches by name"""

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


@sandwiches_r.get("/sandwiches/all")
def get_all_sandwiches() -> dict:
    """Api call that returns all sandwich id's and their name from the database"""

    query = db.get_all_sandwiches()
    if query is None:
        raise HTTPException(404)

    # turn cursor into a dictionary
    # the key is the id
    # the value is the name
    response = {}
    for sandwich in query:
        response[str(sandwich["_id"])] = sandwich["name"]

    return response


@sandwiches_r.get("/sandwiches/top5")
def get_top5() -> list[Sandwich]:
    """Function used in the top 5 sandwiches dash app. Returns a list of the top 5 sandwiches

    Returns:
        list[Sandwich]: the top 5 sandwiches
    """

    # get the id's of the top 5 sandwiches on the platform
    query = db.get_top_5()
    if query is None:
        raise HTTPException(404)

    # get the data for each of them and put it in a list
    top5 = []
    for sandwich in query:
        top5.append(get_sandwich_by_id(sandwich["_id"]))

    # return the list
    return top5
