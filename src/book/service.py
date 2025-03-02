import redis
import json

from typing import Annotated, List, Any
from fastapi import Depends
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from book.model import book
from book.schema import BookCreate

from config import REDIS_HOST, REDIS_PORT

class BookService:
    async def add_book(
        self,
        new_book: Annotated[BookCreate, Depends()], 
        session: AsyncSession = Depends(get_async_session)
    ):
        new_book.cover_path = str(new_book.cover_path)
        stmt = insert(book).values(new_book.model_dump())

        client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0)
        client.set(new_book.name, json.dumps(new_book.model_dump())) #, ex=60)

        await session.execute(stmt)
        await session.commit()
    
    async def get_books(
        self,
        session: AsyncSession = Depends(get_async_session),
    ) -> List[BookCreate]:
        
        query = select(book)
        result = await session.execute(query)
        return result.all()
    
    async def get_books_by_name(
        self,
        name: str,
        session: AsyncSession = Depends(get_async_session),
    ) -> BookCreate:
        client = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=0, decode_responses=True)
        result = client.get(name)
        if result:
            return [json.loads(result)]
        query = select(book).where(book.c.name == name)
        result = await session.execute(query)
        return result.all()