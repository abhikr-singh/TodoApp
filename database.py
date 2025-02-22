from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

SQLALCHEMY_DATABASE_URL = "sqlite:///./todosapp.db"

# SQLALCHEMY_DATABASE_URL = "postgresql://admin:db123@localhost/todo_db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
#
# connect_args={"check_same_thread": False} is used for SQLite databases, to allow the connection to be used by multiple threads.
# engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
