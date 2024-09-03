from sqlalchemy import TIMESTAMP, Column, Integer, String, Table

from database import metadata

book = Table(
    "book",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("author", String),
    Column("cover", String, nullable=True),
    Column("date", TIMESTAMP),
    Column("type", String),
)