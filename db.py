from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql+psycopg2://postgres:postgres@localhost:5432/sqlalchemy_example"

engine = create_engine(DATABASE_URL, echo=True)  # echo=True logs SQL
SessionLocal = sessionmaker(bind=engine)
