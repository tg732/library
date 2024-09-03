from sqlalchemy import TIMESTAMP, Column, Integer, String, Table

from database import metadata

reader = Table(
    "reader",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("phone_number", String),
    Column("photo", String, nullable=True),
    Column("birth_date", TIMESTAMP)
)