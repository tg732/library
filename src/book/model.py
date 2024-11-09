from sqlalchemy import TIMESTAMP, Column, Integer, String, Table

from database import metadata

book = Table(
    "book",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("author", String, nullable=False),
    Column("cover_path", String),
    Column("writing_date", TIMESTAMP(timezone=True)),
    Column("type", String),
)