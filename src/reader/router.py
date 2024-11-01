from typing import Annotated, List, Any
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from reader.model import reader
from reader.schema import ReaderCreate


router = APIRouter(
    prefix="/readers",
    tags=["Reader"]
)

@router.post("/readers")
async def add_reader(
    new_reader: Annotated[ReaderCreate, Depends()], 
    session: AsyncSession = Depends(get_async_session)
):
    print(new_reader.model_dump())
    stmt = insert(reader).values(new_reader.model_dump())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}

@router.get("/readers")
async def get_readers(
    session: AsyncSession = Depends(get_async_session),
) -> List[ReaderCreate]:
    
    query = select(reader)
    result = await session.execute(query)
    return result.all()