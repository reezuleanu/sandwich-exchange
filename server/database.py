from pymongo import MongoClient
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

    def get_sandwich_by_id(self, id: ObjectId) -> Sandwich:
        """Get sandwich data via database ID

        Args:
            id (ObjectId): ID in database

        Returns:
            Sandwich: sandwich data
        """
        query = self.db.sandwiches.find_one({"_id": id})
        if query is not None:
            return Sandwich(**query)
        else:
            return None

    def delete_sandwich_by_id(self, id: ObjectId) -> bool:
        """Delete sandwich data from database via ID

        Args:
            id (ObjectId): Database ID

        Returns:
            bool: return code
        """
        request = self.db.sandwiches.delete_one({"_id": id})
        if request.acknowledged == 1:
            return True
        else:
            return False

    def update_sandwich_by_id(self, id: ObjectId, new_sandwich: Sandwich) -> bool:
        """Update sandwich via ID

        Args:
            id (ObjectId): database id
            new_sandwich(Sandwich): new sandwich data

        Returns:
            bool: return code
        """
        request = self.db.sandwiches.update_one(
            {"_id": id}, {"$set": {**new_sandwich.model_dump()}}
        )
        if request.acknowledged == 1:
            return True
        else:
            return False

    def get_all_sandwiches(self) -> list[Sandwich]:
        """Get all sandwiches from the database

        Returns:
            list[Sandwich]: sandwiches
        """

        query = self.db.sandwiches.find({})
        return query

    def search_sandwiches_by_name(self, sandwich_name: str) -> list[Sandwich]:
        """Query the database by name (not case sensitive, not exact)

        Returns:
            list[Sandwich]: results
        """

        # todo learn to convert cursor to list of sandwiches
        query = self.db.sandwiches.find({"name": sandwich_name})
        return query
