from fastapi import FastAPI
from book.router import router as router_book
from reader.router import router as router_reader

app = FastAPI(
    title="Library"
)

app.include_router(router_book)
app.include_router(router_reader)
