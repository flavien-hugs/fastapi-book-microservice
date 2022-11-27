from pydantic import BaseModel
from typing import List, Optional
from sqlalchemy import MetaData, Column, Integer, String, Table

metadata = MetaData()


class AuthorIn(BaseModel):
    author_name: str
    author_nationality: Optional[str] = None


class AuthorOut(AuthorIn):
    id: int


class AuthorUpdate(AuthorIn):
    author_name: Optional[str] = None
    author_nationality: Optional[str] = None


authors = Table(
    "authors",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("author_name", String(80)),
    Column("author_nationality", String(250)),
)
