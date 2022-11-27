from fastapi import FastAPI

from .api import books, models
from .api.database import database as db, engine

models.metadata.create_all(engine)

app = FastAPI(
    title="Book API",
    openapi_url="/api/v1/books/openapi.json",
    docs_url="/api/v1/books/docs"
)


@app.on_event("startup")
async def startup():
    await db.connect()


@app.on_event("shutdown")
async def shutdown():
    await db.disconnect()


app.include_router(books.books, prefix="/api/v1/books", tags=["books"])


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000, log_level="debug", reload=True)
