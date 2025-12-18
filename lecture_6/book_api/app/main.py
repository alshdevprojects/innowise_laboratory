from typing import Generator, List

from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session

from . import models, schemas, crud
from .database import SessionLocal, engine, Base

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Simple Book Collection API")


@app.get("/healthcheck")
async def healthcheck() -> dict:
         return {"status": "ok"}


# Dependency to get DB session
def get_db() -> Generator[Session, None, None]:
    """
    Yield a database session and ensure it is closed after use.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post(
    "/books/",
    response_model=schemas.Book,
    status_code=status.HTTP_201_CREATED
)
def create_book(
    book: schemas.BookCreate,
    db: Session = Depends(get_db)
) -> schemas.Book:
    """
    Create a new book in the database.
    """
    return crud.create_book(db=db, book=book)


@app.get(
    "/books/",
    response_model=List[schemas.Book]
)
def read_books(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
) -> List[schemas.Book]:
    """
    Retrieve a list of books with optional pagination.
    :param skip: number of records to skip
    :param limit: maximum number of records to return
    """
    return crud.get_books(db=db, skip=skip, limit=limit)


@app.get(
    "/books/{book_id}",
    response_model=schemas.Book
)
def read_book(
    book_id: int,
    db: Session = Depends(get_db)
) -> schemas.Book:
    """
    Retrieve a single book by its ID.
    Raise 404 if the book is not found.
    """
    db_book = crud.get_book(db=db, book_id=book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book


@app.delete(
    "/books/{book_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def remove_book(
    book_id: int,
    db: Session = Depends(get_db)
) -> None:
    """
    Delete a book by its ID.
    Raise 404 if the book is not found.
    Returns 204 No Content on success.
    """
    ok = crud.delete_book(db=db, book_id=book_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Book not found")
    return None
