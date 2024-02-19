from fastapi import FastAPI, HTTPException
from database import db
from models import Sandwich

app = FastAPI()


@app.get("/sandwiches/{sandwich}")
def get_sandwich(sandwich: str) -> Sandwich:
    query = db.sandwiches.find_one({"name": sandwich})
    if query is None:
        raise HTTPException(404, "Sandwich not found")
    return Sandwich(**query)
