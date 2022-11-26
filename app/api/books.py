from typing import List
from sqlalchemy.orm import Session
from fastapi import Header, APIRouter, Depends, HTTPException

from . import db_manager
from .database import database
from .models import BookIn, BookOut

books = APIRouter()


def get_db():
    db = database.SessionLocal()

@books.get("/")
async def index():
    response = {"message": "Welcome to book list"}
    return response


@books.get("/books/", response_model=List[BookOut])
async def list_book():
    return await db_manager.get_all_books()


@books.post("/book/add/", status_code=201)
async def add_book(payload: BookIn):
    book_id = await db_manager.add_book(payload)
    response = {
        "id": book_id,
        **payload.dict()
    }
    return response


@books.put("/book/update/{id}/")
async def update_book(id: int, payload: BookIn):
    book = await db_manager.get_book(id)
    if not book:
        HTTPException(status_code=404, detail="Book not found")
    update_data = payload.dict(exclude_unset=True)
    book_id_db = BookIn(**book)
    update_book = book_id_db.copy(update=update_data)
    return await db_manager.update_book(id, update_book)


@books.delete("/book/delete/{id}/")
async def delete_book(id: int):
    book = await db_manager.get_book(id)
    if not book:
        HTTPException(status_code=404, detail="Book not found")
    return await db_manager.delete_book(id)
