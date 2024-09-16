# database.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define the SQLAlchemy database URL (adjust according to your database)
DATABASE_URL = "sqlite:///./test.db"  
# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL, echo=True)

# Create a base class for declarative models
Base = declarative_base()

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency for creating a new session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
