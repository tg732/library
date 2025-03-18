from typing import List
from fastapi import APIRouter

from book.schema import BookCreate

from book.service import BookService
from dependencies import BookDep, SessionDep

router = APIRouter(
    prefix="/books",
    tags=["Book"]
)

@router.post("/books")
async def add_book(
    new_book: BookDep, 
    session: SessionDep
):
    await BookService().add_book(new_book, session)
    return {"status": "success"}

@router.get("/books")
async def get_books(
    session: SessionDep,
) -> List[BookCreate]:
    
    books = await BookService().get_books(session)
    return books

@router.get("/books/{name}")
async def get_books_by_name(
    name: str,
    session: SessionDep,
) -> List[BookCreate]:
    
    books = await BookService().get_books_by_name(name, session)
    return books