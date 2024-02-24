from pymongo import MongoClient, cursor
from dotenv import load_dotenv
from os import getenv
from .models import Sandwich
from bson import ObjectId

load_dotenv("../.env")


# client = MongoClient(
#     getenv("PYMONGO_DATABASE_HOST"), port=int(getenv("PYMONGO_DATABASE_PORT"))
# )

# db = client.exchange


class Database:
    """MongoDB database interface"""

    def __init__(self) -> None:
        self.client = MongoClient(
            getenv("PYMONGO_DATABASE_HOST"), port=int(getenv("PYMONGO_DATABASE_PORT"))
        )
        self.db = self.client.exchange

    # sandwich CRUD
    def add_sandwich(self, sandwich: Sandwich) -> bool | ObjectId:
        """Add sandwich data to database

        Args:
            sandwich (Sandwich): sandwich data

        Returns:
            bool: return code
            ObjectID: InsertOneResult
        """
        rc = self.db.sandwiches.insert_one(sandwich.model_dump())
        if rc.acknowledged == 1:
            return True, rc.inserted_id
        else:
            return False

    def get_sandwich_by_id(self, sandwich_id: str) -> Sandwich:
        """Get sandwich data via database ID

        Args:
            sandwich_id (str): ID in database

        Returns:
            Sandwich: sandwich data
        """
        query = self.db.sandwiches.find_one({"_id": ObjectId(sandwich_id)})
        if query is not None:
            return Sandwich(**query)
        else:
            return None

    def delete_sandwich_by_id(self, sandwich_id: str) -> bool:
        """Delete sandwich data from database via ID

        Args:
            sandwich_id (str): Database ID

        Returns:
            bool: return code
        """

        if self.db.sandwiches.find_one({"_id": ObjectId(sandwich_id)}) is None:
            return False

        request = self.db.sandwiches.delete_one({"_id": ObjectId(sandwich_id)})
        if request.acknowledged == 1:
            return True
        else:
            return False

    def update_sandwich_by_id(self, sandwich_id: str, new_sandwich: Sandwich) -> bool:
        """Update sandwich via ID

        Args:
            sandwich_id (str): database id
            new_sandwich(Sandwich): new sandwich data

        Returns:
            bool: return code
        """
        request = self.db.sandwiches.update_one(
            {"_id": ObjectId(sandwich_id)}, {"$set": {**new_sandwich.model_dump()}}
        )
        if request.acknowledged == 1:
            return True
        else:
            return False

    def get_all_sandwiches(self) -> cursor:
        """Get all sandwiches from the database

        Returns:
            list[Sandwich]: sandwiches
        """

        # todo make this sorted
        query = self.db.sandwiches.find({}, {"name": 1})
        return query

    def search_sandwiches_by_name(self, sandwich_name: str) -> cursor:
        """Query the database by name (not case sensitive, not exact)

        Returns:
            cursor: results
        """

        query = self.db.sandwiches.find({"name": sandwich_name}, {"name": 1})
        return query
