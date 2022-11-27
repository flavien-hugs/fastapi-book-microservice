from fastapi import FastAPI

from .api import authors, models
from .api.database import database as db, engine

models.metadata.create_all(engine)

app = FastAPI(
    title="Author API",
    openapi_url="/api/v1/authors/openapi.json",
    docs_url="/api/v1/authors/docs"
)


@app.on_event("startup")
async def startup():
    await db.connect()


@app.on_event("shutdown")
async def shutdown():
    await db.disconnect()


app.include_router(authors.authors, prefix="/api/v1/authors", tags=["authors"])


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8001, log_level="debug", reload=True)
