from typing import List
from fastapi import Header, APIRouter

from .models import Book


fake_book_db = [
    {
        'name': 'Star Wars: Episode IX - The Rise of Skywalker',
        'plot': 'The surviving members of the resistance face the First Order once again.',
        'genres': ['Action', 'Adventure', 'Fantasy']
    }
]

books = APIRouter()


@books.get('/')
async def indexPage():
    context = {"message": "Welcome to book microservice api"}
    return context


@books.get('/books/', response_model=List[Book])
async def list_book():
    return fake_book_db


@books.post('/book/add/', status_code=201)
async def add_book(payload: Book):
    book = payload.dict()
    fake_book_db.append(book)
    context = {"id": len(fake_book_db) - 1}
    return context


@books.put('/book/update/{id}/')
async def update_book(id: int, payload: Book):
    book = payload.dict()
    books_length = len(fake_book_db)
    if 0 <= id <= books_length:
        fake_book_db[id] = book
        return None
    return HTTPException(status_code=404, detail="Book with given id not found")


@books.put('/book/delete/{id}/')
async def delete_book(id: int):
    books_length = len(fake_book_db)
    if 0 <= id <= books_length:
        del fake_book_db[id]
        return None
    return HTTPException(status_code=404, detail="Book with given id not found")
