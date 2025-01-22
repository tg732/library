from datetime import datetime
from typing import Optional
from fastapi import File, UploadFile

from pydantic import BaseModel, FilePath, NewPath


class BookCreate(BaseModel):
    id: int
    name: str
    author: str
    cover_path: Optional[str] = None
    writing_date: Optional[datetime] = None
    type: str