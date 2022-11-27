import os
from databases import Database
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from dotenv import dotenv_values

env = dotenv_values(".env")

SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
database = Database(SQLALCHEMY_DATABASE_URL)
