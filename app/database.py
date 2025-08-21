from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql://postgres:2325@localhost/assignit")

Base = declarative_base()

SessionalLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#Dependency for Database Session
def get_db():
    db = SessionalLocal()
    try:
        yield db
    finally:
        db.close()