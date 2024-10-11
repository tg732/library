from datetime import datetime

from pydantic import BaseModel


class ReaderBooksCreate(BaseModel):
    id: int
    book_id: int
    reader_id: int
    is_read: bool
    start_date: datetime
    end_date: datetime

