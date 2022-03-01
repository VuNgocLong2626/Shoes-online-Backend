from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


DATABASE_USER = "root"
DATABASE_PASSWORD = "long2000"
DATABASE_IP_AND_PORT = "localhost:3306"
DATABASE_NAME = "shoes_online"
MYSQL_DATABASE_URL = f"mysql+pymysql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_IP_AND_PORT}/{DATABASE_NAME}"

engine = create_engine(
    MYSQL_DATABASE_URL, echo=True
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()