from typing import List, Any
from fastapi import APIRouter

from dependencies import ReaderDep, SessionDep
from reader.schema import ReaderCreate
from reader.service import ReaderService

router = APIRouter(
    prefix="/readers",
    tags=["Reader"]
)

@router.post("/readers")
async def add_reader(
    new_reader: ReaderDep, 
    session: SessionDep
):
    await ReaderService().add_reader(new_reader, session)
    return {"status": "success"}

@router.get("/readers")
async def get_readers(
    session: SessionDep,
) -> List[ReaderCreate]:
    
    readers = await ReaderService().get_readers(session)
    return readers