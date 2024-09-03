from fastapi import APIRouter
from book.model import book
from book.schema import BookCreate

router = APIRouter(
    prefix="/books",
    tags=["Book"]
)

@router.get("/books")
async def getBooks():
    return [{'bookname_1', 'author_1'}, {'bookname_2', 'author_2'}]
