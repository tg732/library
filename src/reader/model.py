from sqlalchemy import TIMESTAMP, Column, Integer, String, Table

from database import metadata

reader = Table(
    "reader",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("phone_number", String, nullable=False),
    Column("photo", String),
    Column("birth_date", TIMESTAMP(timezone=True))
)