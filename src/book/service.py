from typing import Annotated, List, Any
from fastapi import Depends
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from book.model import book
from book.schema import BookCreate

class BookService:
    async def add_book(
        self,
        new_book: Annotated[BookCreate, Depends()], 
        session: AsyncSession = Depends(get_async_session)
    ):
        new_book.cover_path = str(new_book.cover_path)
        stmt = insert(book).values(new_book.model_dump())
        await session.execute(stmt)
        await session.commit()
    
    async def get_books(
        self,
        session: AsyncSession = Depends(get_async_session),
    ) -> List[BookCreate]:
        
        query = select(book)
        result = await session.execute(query)
        return result.all()