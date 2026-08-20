
from fastapi import APIRouter, HTTPException, status

from src.books.schemas import Book, UpdateBook
from src.books.book_data import book


book_router = APIRouter()


# =========================
# GET ALL BOOKS
# =========================

@book_router.get("/", response_model=list[Book])
async def get_all_books():
    return book


# =========================
# CREATE BOOK
# =========================

@book_router.post("/", response_model=Book,status_code=201)
async def create_book(new_book: Book):

    book.append(new_book.model_dump())

    return new_book


# =========================
# GET BOOK BY ID
# =========================

@book_router.get("/{book_id}", response_model=Book)
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

@book_router.put("/{book_id}", response_model=Book,status_code=200)
async def update_book(
    book_id: int,
    updated_book: Book
) -> Book:

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

@book_router.patch("/{book_id}", response_model=UpdateBook,status_code=200)
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

@book_router.delete("/{book_id}")
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