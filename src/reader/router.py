from typing import Annotated, List, Any
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from reader.model import reader
from reader.schema import ReaderCreate
from reader.service import ReaderService

router = APIRouter(
    prefix="/readers",
    tags=["Reader"]
)

@router.post("/readers")
async def add_reader(
    new_reader: Annotated[ReaderCreate, Depends()], 
    session: AsyncSession = Depends(get_async_session)
):
    await ReaderService().add_reader(new_reader, session)
    return {"status": "success"}

@router.get("/readers")
async def get_readers(
    session: AsyncSession = Depends(get_async_session),
) -> List[ReaderCreate]:
    
    readers = await ReaderService().get_readers(session)
    return readers