from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class ReaderCreate(BaseModel):
    id: int
    name: str
    phone_number: str
    photo: Optional[str] = None
    birth_date: datetime