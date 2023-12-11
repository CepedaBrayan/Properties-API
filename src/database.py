from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from .config import settings

engine = create_engine(settings.db_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


"""
The get_db function is used to generate and return a database session from the database engine.
"""


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
