from typing import List
from sqlalchemy.orm import Session
from fastapi import Header, APIRouter, Depends, HTTPException

from . import db_manager
from .models import BookIn, BookOut

api_book_router = APIRouter()


@api_book_router.get("/", status_code=200)
async def index():
    response = {"message": "Welcome to book list"}
    return response


@api_book_router.get("/books/", response_model=List[BookOut], status_code=200)
async def list_book() -> dict:
    """
    Fetch all books
    """
    return await db_manager.get_all_books()


@api_book_router.get("/book/{book_id}", status_code=200)
async def get_book(book_id: int):
    """
    Fetch a single book by ID
    """
    book = await db_manager.get_book(book_id)
    if not book:
        HTTPException(status_code=404, detail="Book not found")
    response = {"book": book}
    return response


@api_book_router.post("/book/add/", status_code=201)
async def add_book(payload: BookIn):
    """
    Add a book
    """
    book_id = await db_manager.add_book(payload)
    response = {"book_id": book_id, **payload.dict()}
    return response


@api_book_router.put("/book/update/{book_id}/")
async def update_book(book_id: int, payload: BookIn):
    book = await db_manager.get_book(book_id)
    if not book:
        HTTPException(status_code=404, detail="Book not found")
    update_data = payload.dict(exclude_unset=True)
    book_id_db = BookIn(**book)
    update_book = book_id_db.copy(update=update_data)
    return await db_manager.update_book(book_id, update_book)


@api_book_router.delete("/book/delete/{book_id}/")
async def delete_book(book_id: int):
    book = await db_manager.get_book(book_id)
    if not book:
        HTTPException(status_code=404, detail="Book not found")
    return await db_manager.delete_book(book_id)
