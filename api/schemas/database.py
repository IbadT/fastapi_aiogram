from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# URL_DATABASE = 'postgresql://postgres:postgres@localhost/python_tg_game'
# URL_DATABASE = 'postgresql://postgres:postgres@127.0.0.1/python_tg_game'
# URL_DATABASE = 'postgresql://postgres:postgres@database:5432/python_tg_game'
# URL_DATABASE = 'postgresql://postgres:postgres@localhost:5432/python_tg_game'
# URL_DATABASE = 'postgresql://postgres:postgres@127.0.0.1:5432/python_tg_game'
URL_DATABASE = 'postgresql://postgres:postgres@database:5432/python_tg_game'

engine = create_engine(URL_DATABASE)
# database = Database(URL_DATABASE)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()













# from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
# # from pydantic import BaseSettings
# from pydantic import BaseModel
#
# class PostBase(BaseModel):
#     content: str
#     title: str
#
#     class Config:
#         orm_mode = True
#
#
# class CreatePost(PostBase):
#     class Config:
#         orm_mode = True
#
#
#
#
#
#
#
#
#
# class Settings(BaseSettings):
#     database_url: str
#
#     class Config:
#         orm_mode = True
#         env_file = "../.env"
#
# settings = Settings()
#
# DATABASE_URL = settings.database_url
#
# engine = create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base()
#
#




# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"  # SQLite in-memory database for simplicity
# SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:postgres@localhost/fastapi'

# engine = create_async_engine(url=SQLALCHEMY_DATABASE_URL)
# async_session = async_sessionmaker(engine)
# Base = declarative_base()
#
# async def async_main():
#     async with engine.begin() as session:
#         await session.run_sync(Base.metadata.create_all)



# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()