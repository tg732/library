from typing import Annotated, List
from fastapi import Depends
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from reader.model import reader
from reader.schema import ReaderCreate


class ReaderService:
    async def add_reader(
        self,
        new_reader: Annotated[ReaderCreate, Depends()], 
        session: AsyncSession = Depends(get_async_session)
    ):
        stmt = insert(reader).values(new_reader.model_dump())
        await session.execute(stmt)
        await session.commit()

    async def get_readers(
        self,
        session: AsyncSession = Depends(get_async_session),
    ) -> List[ReaderCreate]:
        
        query = select(reader)
        result = await session.execute(query)
        return result.all()