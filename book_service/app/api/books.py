from typing import List
from fastapi import APIRouter, HTTPException

from . import db_manager
from .service import is_author_present
from .models import BookIn, BookOut, BookUpdate

books = APIRouter()


@books.get("/", response_model=List[BookOut], status_code=200)
async def list_book() -> dict:
    """
    Fetch all books
    """
    return await db_manager.get_all_books()


@books.get("/{book_id}", response_model=BookOut, status_code=200)
async def get_book(book_id: int):
    """
    Fetch a single book by ID
    """
    book = await db_manager.get_book(book_id)
    if not book:
        HTTPException(status_code=404, detail="Book not found")
    return book


@books.post("/create/", response_model=BookOut, status_code=201)
async def create_book(payload: BookIn):
    """
    Create a book
    """
    for author_id in payload.authors_id:
        if not is_author_present(author_id):
            raise HTTPException(
                status_code=404,
                detail=f"Author with id:{author_id} not found")

    book_id = await db_manager.add_book(payload)
    response = {"id": book_id, **payload.dict()}
    return response


@books.put("/update/{book_id}/", response_model=BookOut)
async def update_book(book_id: int, payload: BookUpdate):
    book = await db_manager.get_book(book_id)

    if not book:
        HTTPException(status_code=404, detail="Book not found")

    update_data = payload.dict(exclude_unset=True)
    if "authors_id" in update_data:
        for author_id in payload.authors_id:
            if not is_author_present(author_id):
                raise HTTPException(
                    status_code=404,
                    detail=f"Author with given id:{author_id} not found")

    book_id_db = BookIn(**book)
    update_book = book_id_db.copy(update=update_data)
    return await db_manager.update_book(book_id, update_book)


@books.delete("/delete/{book_id}/", response_model=None)
async def delete_book(book_id: int):
    book = await db_manager.get_book(book_id)
    if not book:
        HTTPException(status_code=404, detail="Book not found")
    return await db_manager.delete_book(book_id)
