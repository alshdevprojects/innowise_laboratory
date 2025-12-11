from typing import List, Optional

from sqlalchemy.orm import Session

from . import models, schemas


def get_book(db: Session, book_id: int) -> Optional[models.Book]:
    """
    Retrieve a single book by its ID.

    :param db: SQLAlchemy Session object
    :param book_id: ID of the book to retrieve
    :return: Book object if found, else None
    """
    return db.query(models.Book).filter(models.Book.id == book_id).first()


def get_books(db: Session, skip: int = 0, limit: int = 100) -> List[models.Book]:
    """
    Retrieve a list of books with pagination.

    :param db: SQLAlchemy Session object
    :param skip: Number of records to skip
    :param limit: Maximum number of records to return
    :return: List of Book objects
    """
    return db.query(models.Book).offset(skip).limit(limit).all()


def create_book(db: Session, book: schemas.BookCreate) -> models.Book:
    """
    Create a new book record in the database.

    :param db: SQLAlchemy Session object
    :param book: BookCreate schema containing book details
    :return: The newly created Book object
    """
    db_book = models.Book(title=book.title, author=book.author, year=book.year)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


def delete_book(db: Session, book_id: int) -> bool:
    """
    Delete a book by its ID.

    :param db: SQLAlchemy Session object
    :param book_id: ID of the book to delete
    :return: True if the book was deleted, False if not found
    """
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if db_book:
        db.delete(db_book)
        db.commit()
        return True
    return False
