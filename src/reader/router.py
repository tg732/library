from fastapi import APIRouter
from reader.model import reader
from reader.schema import ReaderCreate

router = APIRouter(
    prefix="/readers",
    tags=["Reader"]
)

@router.get("/readers")
async def getReaders():
    return [{'bookname_1', 'author_1'}, {'bookname_2', 'author_2'}]

