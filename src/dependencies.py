from typing import Annotated
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from book.schema import BookCreate
from reader.schema import ReaderCreate
from reader_books.schema import ReaderBooksCreate


SessionDep = Annotated[AsyncSession, Depends(get_async_session)]
BookDep = Annotated[BookCreate, Depends()]
ReaderDep = Annotated[ReaderCreate, Depends()]
ReaderBooksDep = Annotated[ReaderBooksCreate, Depends()]