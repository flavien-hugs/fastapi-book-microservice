from pydantic import BaseModel
from typing import List, Optional
from sqlalchemy import MetaData, Column, Integer, String, Table, ARRAY

metadata = MetaData()

books = Table(
    "books",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("author_name", String(80)),
    Column("book_description", String(250)),
    Column("book_genres", ARRAY(String)),
)


class BookIn(BaseModel):
    author_name: str
    book_description: str
    book_genres: List[str]


class BookOut(BookIn):
    id: int


class BookUpdate(BookIn):
    author_name: str
    book_description: str
    book_genres: List[str]
