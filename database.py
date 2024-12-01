from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLite database URL (this is correct for SQLite)
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"  # Relative path to the SQLite DB file

# Create the engine for the SQLite database
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# SessionLocal is a session factory for creating new sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for the models, which will be used to define your tables
Base = declarative_base()

# Dependency for getting the DB session, used with FastAPI's Depends()
def get_db():
    db = SessionLocal()  # Create a session
    try:
        yield db  # Yield it to the request handler
    finally:
        db.close()  # Close the session when done
