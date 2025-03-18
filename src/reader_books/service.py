from typing import List
from sqlalchemy import insert, select

from dependencies import ReaderBooksDep, SessionDep
from reader_books.model import reader_books
from reader_books.schema import ReaderBooksCreate

class ReaderBooksService:
    async def add_readers_book(
        self,
        new_reader_books: ReaderBooksDep, 
        session: SessionDep
    ):
        stmt = insert(reader_books).values(new_reader_books.model_dump())
        await session.execute(stmt)
        await session.commit()

    async def get_readers_books(
        self,
        session: SessionDep,
    ) -> List[ReaderBooksCreate]:
        
        query = select(reader_books)
        result = await session.execute(query)
        return result.all()