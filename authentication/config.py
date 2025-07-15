from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
DATABASE_URL = "mysql+pymysql://root:Nec020602%40123@localhost:3306/auth"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# jwt
SECRET_KEY = "1213c9f6-ff10-47dd-a410-efa42cb3957b"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30