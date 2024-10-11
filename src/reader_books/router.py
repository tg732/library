from typing import List, Any
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from reader_books.model import reader_books
from reader_books.schema import ReaderBooksCreate

router = APIRouter(
    prefix="/reader_books",
    tags=["ReaderBooks"]
)

# @router.get("/books")
# async def getbooks():
#     return [{'bookname_1', 'author_1'}, {'bookname_2', 'author_2'}]

@router.post("/reader_books")
async def add_book(new_reader_books: ReaderBooksCreate, session: AsyncSession = Depends(get_async_session)):
    print(new_reader_books.model_dump())
    stmt = insert(reader_books).values(new_reader_books.model_dump())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}

@router.get("/reader_books")
async def get_books(
    session: AsyncSession = Depends(get_async_session),
) -> List[ReaderBooksCreate]:
    
    query = select(reader_books)
    result = await session.execute(query)
    return result.all()