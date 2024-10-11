from sqlalchemy import TIMESTAMP, Column, Integer, String, Table, Boolean, ForeignKey

from database import metadata

reader_books = Table(
    "reader_books",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("book_id", Integer, ForeignKey("book.id"), nullable=False),
    Column("reader_id", Integer, ForeignKey("reader.id"), nullable=False),
    Column("is_read", Boolean),
    Column("start_date", TIMESTAMP(timezone=True)),
    Column("end_date", TIMESTAMP(timezone=True)),
)