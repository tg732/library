from typing import Annotated, List, Any
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from reader_books.model import reader_books
from reader_books.schema import ReaderBooksCreate
from reader_books.service import ReaderBooksService

router = APIRouter(
    prefix="/reader_books",
    tags=["ReaderBooks"]
)

@router.post("/reader_books")
async def add_book(
    new_reader_books: Annotated[ReaderBooksCreate, Depends()], 
    session: AsyncSession = Depends(get_async_session)
):
    await ReaderBooksService().add_book(new_reader_books, session)
    return {"status": "success"}

@router.get("/reader_books")
async def get_books(
    session: AsyncSession = Depends(get_async_session),
) -> List[ReaderBooksCreate]:
    
    readerBooks = await ReaderBooksService().get_books(session)
    return readerBooks