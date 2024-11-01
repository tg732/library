from datetime import date
from typing import Optional
from fastapi import File, UploadFile

from pydantic import BaseModel


class BookCreate(BaseModel):
    id: int
    name: str
    author: str
    cover: Optional[UploadFile] = None
    writing_date: Optional[date] = None
    type: str