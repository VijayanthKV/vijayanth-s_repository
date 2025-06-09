from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

#Database URL 
SQLALCHEMY_DATABASE_URL = 'sqlite:///./test.db'

#Creating engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False}
)

#Initializing sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#Declaring base class to inherit at model creation
Base = declarative_base()

#session control
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()