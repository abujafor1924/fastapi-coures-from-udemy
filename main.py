

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

app = FastAPI()

book = [
  {
    "id": 1,
    "author": "George Orwell",
    "name": "1984",
    "publisher": "Secker & Warburg",
    "publish_date": "1949-06-08",
    "page_count": 328,
    "language": "English"
  },
  {
    "id": 2,
    "author": "J.K. Rowling",
    "name": "Harry Potter and the Philosopher's Stone",
    "publisher": "Bloomsbury",
    "publish_date": "1997-06-26",
    "page_count": 223,
    "language": "English"
  },
  {
    "id": 3,
    "author": "Harper Lee",
    "name": "To Kill a Mockingbird",
    "publisher": "J. B. Lippincott & Co.",
    "publish_date": "1960-07-11",
    "page_count": 281,
    "language": "English"
  },
  {
    "id": 4,
    "author": "F. Scott Fitzgerald",
    "name": "The Great Gatsby",
    "publisher": "Charles Scribner's Sons",
    "publish_date": "1925-04-10",
    "page_count": 180,
    "language": "English"
  },
  {
    "id": 5,
    "author": "Paulo Coelho",
    "name": "The Alchemist",
    "publisher": "HarperTorch",
    "publish_date": "1988-01-01",
    "page_count": 208,
    "language": "Portuguese"
  },
  {
    "id": 6,
    "author": "Rabindranath Tagore",
    "name": "Gitanjali",
    "publisher": "Macmillan",
    "publish_date": "1910-08-14",
    "page_count": 157,
    "language": "Bengali"
  },
  {
    "id": 7,
    "author": "Leo Tolstoy",
    "name": "War and Peace",
    "publisher": "The Russian Messenger",
    "publish_date": "1869-01-01",
    "page_count": 1225,
    "language": "Russian"
  },
  {
    "id": 8,
    "author": "Ernest Hemingway",
    "name": "The Old Man and the Sea",
    "publisher": "Charles Scribner's Sons",
    "publish_date": "1952-09-01",
    "page_count": 128,
    "language": "English"
  },
  {
    "id": 9,
    "author": "Victor Hugo",
    "name": "Les Misérables",
    "publisher": "A. Lacroix",
    "publish_date": "1862-01-01",
    "page_count": 1463,
    "language": "French"
  },
  {
    "id": 10,
    "author": "Khaled Hosseini",
    "name": "The Kite Runner",
    "publisher": "Riverhead Books",
    "publish_date": "2003-05-29",
    "page_count": 371,
    "language": "English"
  }
]