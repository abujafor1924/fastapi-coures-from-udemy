

# from fastapi import FastAPI,Header,Request
# from typing import Optional
# from httpx import post
# from pydantic import BaseModel


# app=FastAPI()

# @app.get("/")
# async def read_root():
#     return {"message": "Hello World"}


# @app.get("/greet")
# async def greet_name(name:Optional[str] = "User", age:Optional[int] = 0)-> dict:
#     if name is None:
#         name = "World"
#     if age is None:
#         age = 0
#     return {"message": f"Hello {name} age {age}"}



# class BookCreateModel(BaseModel):
#     title: str
#     author: str
#     year: Optional[int] = None

# @app.post("/create_book")
# async def create_book(book: BookCreateModel) -> dict:
#     book_info = {
#         "title": book.title,
#         "author": book.author,
#         "year": book.year if book.year is not None else "Unknown"
#     }
#     return {"message": "Book created successfully", "book": book_info}



# @app.get("/get_headers",status_code=201)
# async def get_headers(
#     request: Request,
#     accept: str = Header(None),
#     user_agent: str = Header(None),
#     content_type: str = Header(None)
# ) -> dict:

#     requested_headers = {
#         "Accept": accept,
#         "User-Agent": user_agent,
#         "Content-Type": content_type,
#         "Host": request.headers.get("Host")
#     }

#     return {"headers": requested_headers}



from fastapi import FastAPI
from src.books.routes import book_router

version = "v1"

app = FastAPI(
    title="Bookly",
    description="A REST API for a book",
    version=version
)

app.include_router(book_router,prefix=f"/api/{version}/books",tags=["Books"])







