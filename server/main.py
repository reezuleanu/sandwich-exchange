from fastapi import FastAPI, HTTPException
from .routes import index_r, sandwiches_r

app = FastAPI()

app.include_router(index_r)
app.include_router(sandwiches_r)
