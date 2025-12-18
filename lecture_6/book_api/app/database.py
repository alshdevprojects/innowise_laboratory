from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Database URL: using SQLite database file located in the project root
SQLALCHEMY_DATABASE_URL: str = "sqlite:///./books.db"

# Create SQLAlchemy engine
# connect_args is needed only for SQLite in single-thread mode
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Create a configured "Session" class
# autocommit=False: changes are not committed automatically
# autoflush=False: changes are not flushed automatically to the database
# bind=engine: associate session with the engine
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for declarative class definitions
# Models will inherit from this Base to create database tables
Base = declarative_base()