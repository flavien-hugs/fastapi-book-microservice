from typing import List
from fastapi import APIRouter, HTTPException

from . import db_manager
from .models import AuthorOut, AuthorIn, AuthorUpdate

authors = APIRouter()


@authors.get("/", response_model=List[AuthorOut], status_code=200)
async def list_author() -> dict:
    """
    Fetch all authors
    """
    return await db_manager.get_all_authors()


@authors.post('/create/', response_model=AuthorOut, status_code=201)
async def create_author(payload: AuthorIn):
    author_id = await db_manager.add_author(payload)

    response = {
        'id': author_id,
        **payload.dict()
    }

    return response


@authors.get('/{author_id}/', response_model=AuthorOut)
async def get_author(author_id: int):
    author = await db_manager.get_author(author_id)
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")
    return author


@authors.put("/update/{author_id}/", response_model=AuthorOut)
async def update_author(author_id: int, payload: AuthorUpdate):
    author = await db_manager.get_author(author_id)

    if not author:
        HTTPException(status_code=404, detail="Author not found")

    update_data = payload.dict(exclude_unset=True)
    author_id_db = AuthorIn(**author)
    update_author = author_id_db.copy(update=update_data)
    return await db_manager.update_author(author_id, update_author)


@authors.delete("/delete/{author_id}/", response_model=None)
async def delete_author(author_id: int):
    author = await db_manager.get_author(author_id)
    if not author:
        HTTPException(status_code=404, detail="Author not found")
    return await db_manager.delete_author(author_id)
