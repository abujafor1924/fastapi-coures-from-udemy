from pydantic import BaseModel

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