import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Use the DATABASE_URL from environment or fallback to local
database_url = os.environ.get("DATABASE_URL", "postgresql://postgres:1234@localhost:5432/fastapi")

# Create the engine with pre-ping enabled
engine = create_engine(database_url, echo=True, pool_pre_ping=True)

# Session and base for ORM
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
