import os

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker
 
from dotenv import load_dotenv



load_dotenv('.env')

DB_DRIVE = os.getenv('DB_DRIVE')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = int(os.getenv('DB_PORT'))
DB_NAME = os.getenv('DB_NAME')


if None in [DB_DRIVE, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME]:
    raise ValueError('One or more required enviroment variables are not set')


SQLALCHEMY_DB_URL = f'{DB_DRIVE}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'


engine = create_engine(SQLALCHEMY_DB_URL, echo=True)


SessionLocal = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass