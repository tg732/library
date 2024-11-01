from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class ReaderBooksCreate(BaseModel):
    id: int
    book_id: int
    reader_id: int
    is_read: bool
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None

