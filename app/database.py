from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

engine = create_engine(f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}/{settings.database_name}")

Base = declarative_base()

SessionalLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#Dependency for Database Session
def get_db():
    db = SessionalLocal()
    try:
        yield db
    finally:
        db.close()