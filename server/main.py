from fastapi import FastAPI, HTTPException
from database import Database
from models import Sandwich

app = FastAPI()
db = Database()
