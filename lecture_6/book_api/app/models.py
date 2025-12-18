from sqlalchemy import Column, Integer, String
from .database import Base


class Book(Base):
    """
    SQLAlchemy model for the 'books' table.

    Attributes:
        id (int): Primary key, unique book identifier.
        title (str): Title of the book, required.
        author (str): Author of the book, required.
        year (int, optional): Year of publication.
    """

    __tablename__ = "books"

    id: int = Column(Integer, primary_key=True, index=True)
    title: str = Column(String, nullable=False, index=True)
    author: str = Column(String, nullable=False, index=True)
    year: int | None = Column(Integer, nullable=True)
