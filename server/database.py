from pymongo import MongoClient, cursor, TEXT, collation
from dotenv import load_dotenv
from os import getenv
from .models import Sandwich
from bson import ObjectId


class Database:
    """MongoDB database interface"""

    def __init__(self) -> None:
        # load_dotenv("../.env")
        self.client = MongoClient(
            getenv("PYMONGO_DATABASE_HOST"), port=int(getenv("PYMONGO_DATABASE_PORT"))
        )
        # self.client = MongoClient(host="127.0.0.1", port=27017)
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

    def get_all_sandwiches(self, limit: int | None = 0) -> cursor:
        """Get all sandwiches from the database

        Args:
            limit (int | None, optional): Optional results limit. Defaults to 0.

        Returns:
            cursor: results
        """

        query = (
            self.db.sandwiches.find({}, {"name": 1}).sort({"price": -1}).limit(limit)
        )
        return query

    def search_sandwiches_by_name(self, sandwich_name: str) -> cursor:
        """Query the database by name (not case sensitive, not exact)

        Returns:
            cursor: results
        """

        # create index for name, inexact
        self.db.sandwiches.create_index(
            (["name", TEXT]), collation=collation.Collation(locale="en", strength=2)
        )

        # query for name, case insensitive
        query = self.db.sandwiches.find(
            {"name": {"$regex": sandwich_name, "$options": "i"}}, {"name": 1}
        )

        return query

    def get_top_5(self) -> cursor:
        """Get the top 5 documents based on price

        Returns:
            cursor: results
        """

        query = self.db.sandwiches.find({}).sort({"price": -1}).limit(5)

        return query
