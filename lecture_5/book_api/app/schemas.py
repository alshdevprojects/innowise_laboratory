from typing import Optional
from pydantic import BaseModel


class BookBase(BaseModel):
    """
    Base schema for a book.

    Attributes:
        title (str): Title of the book.
        author (str): Author of the book.
        year (Optional[int]): Year of publication, optional.
    """
    title: str
    author: str
    year: Optional[int] = None


class BookCreate(BookBase):
    """
    Schema for creating a new book.

    Inherits all fields from BookBase.
    """
    pass


class Book(BookBase):
    """
    Schema for reading a book from the database.

    Attributes:
        id (int): Unique identifier of the book.
    """
    id: int

    class Config:
        # Enable ORM mode to allow reading data from SQLAlchemy models
        orm_mode = True
