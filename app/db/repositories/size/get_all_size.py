from sqlalchemy import false
from app.db.database import SessionLocal
from app.db.tables import Size


db = SessionLocal()


def get_all_size():
    size_all = db.query(Size).order_by(Size.size_number).all()
    db.close()
    return size_all