from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase


url="sqlite:///./notes.db"

engine=create_engine(url, connect_args={"check_same_thread":False})

SessionLocal=sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass


def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()