import redis
import json

from typing import List
from sqlalchemy import insert, select

from book.model import book
from book.schema import BookCreate

from config import REDIS_HOST, REDIS_PORT
from dependencies import BookDep, SessionDep

class BookService:
    async def add_book(
        self,
        new_book: BookDep, 
        session: SessionDep
    ):
        new_book.cover_path = str(new_book.cover_path)
        stmt = insert(book).values(new_book.model_dump())

        client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0)
        client.set(new_book.name, json.dumps(new_book.model_dump())) #, ex=60)

        await session.execute(stmt)
        await session.commit()
    
    async def get_books(
        self,
        session: SessionDep,
    ) -> List[BookCreate]:
        
        query = select(book)
        result = await session.execute(query)
        return result.all()
    
    async def get_books_by_name(
        self,
        name: str,
        session: SessionDep,
    ) -> BookCreate:
        client = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=0, decode_responses=True)
        result = client.get(name)
        if result:
            return [json.loads(result)]
        query = select(book).where(book.c.name == name)
        result = await session.execute(query)
        return result.all()