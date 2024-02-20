from pymongo import MongoClient
from dotenv import load_dotenv
from os import getenv

load_dotenv("../.env")


client = MongoClient(
    getenv("PYMONGO_DATABASE_HOST"), port=int(getenv("PYMONGO_DATABASE_PORT"))
)

db = client.exchange
