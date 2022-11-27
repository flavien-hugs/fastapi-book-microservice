from pydantic import BaseModel
from typing import List, Optional
from sqlalchemy import MetaData, Column, Integer, String, Table, ARRAY

metadata = MetaData()


class BookIn(BaseModel):
    book_title: str
    book_description: str
    book_genres: List[str]
    authors_id: List[int]


class BookOut(BookIn):
    id: int


class BookUpdate(BookIn):
    book_title: Optional[str] = None
    book_description: Optional[str] = None
    book_genres: Optional[List[str]] = None
    authors_id: Optional[List[str]] = None


books = Table(
    "books",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("book_title", String(80)),
    Column("book_description", String(250)),
    Column("book_genres", ARRAY(String)),
    Column("authors_id", ARRAY(Integer)),
)
