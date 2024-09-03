from datetime import datetime

from pydantic import BaseModel


class BookCreate(BaseModel):
    id: int
    name: str
    author: str
    cover: str
    date: datetime
    type: str