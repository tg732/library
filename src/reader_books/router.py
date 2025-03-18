from typing import List
from fastapi import APIRouter

from dependencies import ReaderBooksDep, SessionDep
from reader_books.schema import ReaderBooksCreate
from reader_books.service import ReaderBooksService

router = APIRouter(
    prefix="/reader_books",
    tags=["ReaderBooks"]
)

@router.post("/reader_books")
async def add_readers_book(
    new_reader_books: ReaderBooksDep, 
    session: SessionDep
):
    await ReaderBooksService().add_readers_book(new_reader_books, session)
    return {"status": "success"}

@router.get("/reader_books")
async def get_readers_books(
    session: SessionDep,
) -> List[ReaderBooksCreate]:
    
    readerBooks = await ReaderBooksService().get_readers_books(session)
    return readerBooks