from fastapi import FastAPI

from . import books, models
from .api.database import database as db, engine

models.metadata.create_all(engine)

app = FastAPI()


@app.on_event("startup")
async def startup():
    await db.connect()


@app.on_event("shutdown")
async def shutdown():
    await db.disconnect()


app.include_router(books)
