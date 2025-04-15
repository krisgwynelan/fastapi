import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Fetch the database URL from environment variables
database_url = os.environ.get("DATABASE_URL", "postgresql://postgres:1234@localhost:5432/fastapi")

engine = create_engine(database_url, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
