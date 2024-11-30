from typing import Annotated, List
from fastapi import Depends
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from reader_books.model import reader_books
from reader_books.schema import ReaderBooksCreate

class ReaderBooksService:
    async def add_book(
        self,
        new_reader_books: Annotated[ReaderBooksCreate, Depends()], 
        session: AsyncSession = Depends(get_async_session)
    ):
        stmt = insert(reader_books).values(new_reader_books.model_dump())
        await session.execute(stmt)
        await session.commit()

    async def get_books(
        self,
        session: AsyncSession = Depends(get_async_session),
    ) -> List[ReaderBooksCreate]:
        
        query = select(reader_books)
        result = await session.execute(query)
        return result.all()