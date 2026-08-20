

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

from fastapi import FastAPI, HTTPException,status
from pydantic import BaseModel
from typing import List

app = FastAPI()


# =========================
# BOOK DATA
# =========================

book = [
    {
        "id": 1,
        "author": "George Orwell",
        "title": "1984",
        "publisher": "Secker & Warburg",
        "publish_date": "1949-06-08",
        "page_count": 328,
        "language": "English"
    },
    {
        "id": 2,
        "author": "J.K. Rowling",
        "title": "Harry Potter and the Philosopher's Stone",
        "publisher": "Bloomsbury",
        "publish_date": "1997-06-26",
        "page_count": 223,
        "language": "English"
    },
    {
        "id": 3,
        "author": "Harper Lee",
        "title": "To Kill a Mockingbird",
        "publisher": "J. B. Lippincott & Co.",
        "publish_date": "1960-07-11",
        "page_count": 281,
        "language": "English"
    },
    {
        "id": 4,
        "author": "F. Scott Fitzgerald",
        "title": "The Great Gatsby",
        "publisher": "Charles Scribner's Sons",
        "publish_date": "1925-04-10",
        "page_count": 180,
        "language": "English"
    },
    {
        "id": 5,
        "author": "Paulo Coelho",
        "title": "The Alchemist",
        "publisher": "HarperTorch",
        "publish_date": "1988-01-01",
        "page_count": 208,
        "language": "Portuguese"
    },
    {
        "id": 6,
        "author": "Rabindranath Tagore",
        "title": "Gitanjali",
        "publisher": "Macmillan",
        "publish_date": "1910-08-14",
        "page_count": 157,
        "language": "Bengali"
    },
    {
        "id": 7,
        "author": "Leo Tolstoy",
        "title": "War and Peace",
        "publisher": "The Russian Messenger",
        "publish_date": "1869-01-01",
        "page_count": 1225,
        "language": "Russian"
    },
    {
        "id": 8,
        "author": "Ernest Hemingway",
        "title": "The Old Man and the Sea",
        "publisher": "Charles Scribner's Sons",
        "publish_date": "1952-09-01",
        "page_count": 128,
        "language": "English"
    },
    {
        "id": 9,
        "author": "Victor Hugo",
        "title": "Les Misérables",
        "publisher": "A. Lacroix",
        "publish_date": "1862-01-01",
        "page_count": 1463,
        "language": "French"
    },
    {
        "id": 10,
        "author": "Khaled Hosseini",
        "title": "The Kite Runner",
        "publisher": "Riverhead Books",
        "publish_date": "2003-05-29",
        "page_count": 371,
        "language": "English"
    }
]


# =========================
# PYDANTIC MODEL
# =========================

class Book(BaseModel):
    id: int
    author: str
    title: str
    publisher: str
    publish_date: str
    page_count: int
    language: str




class UpdateBook(BaseModel):
    author: str | None = None
    title: str | None = None
    publisher: str | None = None
    page_count: int | None = None
    language: str | None = None


# =========================
# GET ALL BOOKS
# =========================

@app.get("/books", response_model=List[Book])
async def get_all_books():
    return book


# =========================
# CREATE BOOK
# =========================

@app.post("/books", response_model=Book,status_code=201)
async def create_book(new_book: Book):

    book.append(new_book.model_dump())

    return new_book


# =========================
# GET BOOK BY ID
# =========================

@app.get("/books/{book_id}", response_model=Book)
async def get_book_by_id(book_id: int) -> Book:

    for b in book:

        if b["id"] == book_id:
            return b

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Book not found"
    )


# =========================
# UPDATE BOOK - PUT
# =========================

@app.put("/books/{book_id}", response_model=UpdateBook,status_code=200)
async def update_book(
    book_id: int,
    updated_book: UpdateBook
) -> UpdateBook:

    for b in book:

        if b["id"] == book_id:

            b.update(updated_book.model_dump())

            return b

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Book not found"
    )


# =========================
# PARTIAL UPDATE - PATCH
# =========================

@app.patch("/books/{book_id}", response_model=UpdateBook,status_code=200)
async def partial_update_book(
    book_id: int,
    updated_fields: UpdateBook
) -> UpdateBook:

    for b in book:

        if b["id"] == book_id:

            b.update(updated_fields.model_dump())

            return b

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Book not found"
    )


# =========================
# DELETE BOOK
# =========================

@app.delete("/books/{book_id}")
async def delete_book(book_id: int) -> dict:

    for b in book:

        if b["id"] == book_id:

            book.remove(b)

            return {
                "message": "Book deleted successfully"
            }

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Book not found"
    )