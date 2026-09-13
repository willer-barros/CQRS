import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')

if not DATABASE_URL:
    raise ValueError("Variavel do db de escrita nao localizada")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


MONGO_URL = os.getenv("MONGO_URL")

if not MONGO_URL:
    raise ValueError("Variavel do db de leitura nao localizada")

mongo_client = MongoClient(MONGO_URL)
mongo_db = mongo_client["primeiro"]

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()