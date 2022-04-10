from sqlalchemy import false
from app.db.database import SessionLocal
from app.db.tables import Size


db = SessionLocal()


def get_size_by_number(number: int):
    size_all = db.query(Size).filter(Size.size_number == number).first()
    db.close()
    return size_all