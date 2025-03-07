from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Kết nối SQLite
DATABASE_URL = "sqlite:///test.db"
engine = create_engine(DATABASE_URL, echo=False)

# Base model
Base = declarative_base()

# Session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Hàm tạo database
def init_db():
    Base.metadata.create_all(bind=engine)
