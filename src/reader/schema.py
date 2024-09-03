from datetime import datetime

from pydantic import BaseModel


class ReaderCreate(BaseModel):
    id: int
    name: str
    phone_number: str
    photo: str
    birth_date: datetime