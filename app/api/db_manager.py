from .database import database
from .models import books, BookIn, BookOut, BookUpdate


async def add_book(payload: BookIn):
    query = books.insert().values(**payload.dict())
    return await database.execute(query=query)


async def get_all_books():
    query = books.select()
    return await database.fetch_all(query=query)


async def get_book(id):
    query = books.select(books.c.id == id)
    return await database.fetch_one(query=query)


async def delete_book(id: int):
    query = books.delete().where(books.c.id == id)
    return await database.execute(query=query)


async def update_book(id: int, payload: BookIn):
    query = books.update().where(books.c.id == id).values(**payload.dict())
    return await database.execute(query=query)
