from typing import Annotated, List, Any
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from book.model import book
from book.schema import BookCreate

router = APIRouter(
    prefix="/books",
    tags=["Book"]
)

@router.post("/books")
async def add_book(
    new_book: Annotated[BookCreate, Depends()], 
    session: AsyncSession = Depends(get_async_session)
):
    print(new_book.model_dump())
    file = new_book.cover
    new_book.cover = new_book.cover.filename
    stmt = insert(book).values(new_book.model_dump())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}

@router.get("/books")
async def get_books(
    session: AsyncSession = Depends(get_async_session),
) -> List[BookCreate]:
    
    query = select(book)
    result = await session.execute(query)
    return result.all()