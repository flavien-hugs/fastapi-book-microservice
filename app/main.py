from fastapi import FastAPI

from .api.books import books

app = FastAPI()

app.include_router(books)
