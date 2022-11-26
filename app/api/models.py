from typing import List
from pydantic import BaseModel


class Book(BaseModel):
    name: str
    plot: str
    genres: List[str]
