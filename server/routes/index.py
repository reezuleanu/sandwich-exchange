from fastapi import APIRouter


index_r = APIRouter()


@index_r.get("/")
def index() -> None:
    return {"response": "hello there"}
