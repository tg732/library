from contextlib import asynccontextmanager
from fastapi import FastAPI
import uvicorn
from book.router import router as router_book
from reader.router import router as router_reader
from reader_books.router import router as router_reader_books

from database import create_tables, delete_tables

@asynccontextmanager
async def lifespan(app: FastAPI):
    # await delete_tables()
    # print("База очищена")
    await create_tables()
    print("База готова к работе")
    yield
    print("Выключение")
    

app = FastAPI(
    title="Library",
    lifespan=lifespan
)

app.include_router(router_book)
app.include_router(router_reader)
app.include_router(router_reader_books)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)