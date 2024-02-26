from fastapi import FastAPI, HTTPException
from .routes import index_r, sandwiches_r

# ! This should be run with uvicorn within the sandwich-exchange folder


# initiate app
app = FastAPI()

# add routers
app.include_router(index_r)
app.include_router(sandwiches_r)
