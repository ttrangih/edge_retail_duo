import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = os.getenv("postgresql://edge_retail_db_user:TlWs9AEEitg8SnJJjsgkg4QaM7fsAlxX@dpg-d0m8k5h5pdvs7391auvg-a/edge_retail_db")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()