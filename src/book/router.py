from typing import Annotated, List, Any
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from book.schema import BookCreate

from book.service import BookService

router = APIRouter(
    prefix="/books",
    tags=["Book"]
)

@router.post("/books")
async def add_book(
    new_book: Annotated[BookCreate, Depends()], 
    session: AsyncSession = Depends(get_async_session)
):
    await BookService().add_book(new_book, session)
    return {"status": "success"}

@router.get("/books")
async def get_books(
    session: AsyncSession = Depends(get_async_session),
) -> List[BookCreate]:
    
    books = await BookService().get_books(session)
    return books

@router.get("/books/{name}")
async def get_books_by_name(
    name: str,
    session: AsyncSession = Depends(get_async_session),
) -> List[BookCreate]:
    
    books = await BookService().get_books_by_name(name, session)
    return books