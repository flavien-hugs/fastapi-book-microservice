from databases import Database
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from dotenv import dotenv_values

env = dotenv_values(".env")

DB_USERNAME = env.get("DB_USERNAME")
DB_PASSWORD = env.get("DB_PASSWORD")
DB_NAME = env.get("DB_NAME")

SQLALCHEMY_DATABASE_URL = (
    f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@localhost/{DB_NAME}"
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
database = Database(SQLALCHEMY_DATABASE_URL)
