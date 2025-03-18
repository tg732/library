from typing import List
from sqlalchemy import insert, select

from dependencies import ReaderDep, SessionDep
from reader.model import reader
from reader.schema import ReaderCreate


class ReaderService:
    async def add_reader(
        self,
        new_reader: ReaderDep, 
        session: SessionDep
    ):
        stmt = insert(reader).values(new_reader.model_dump())
        await session.execute(stmt)
        await session.commit()

    async def get_readers(
        self,
        session: SessionDep,
    ) -> List[ReaderCreate]:
        
        query = select(reader)
        result = await session.execute(query)
        return result.all()