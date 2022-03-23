from sqlalchemy import false
from app.db.database import SessionLocal
from app.db.tables import Color


db = SessionLocal()


def get_all_color():
    db.close()
    color_all = db.query(Color).all()
    return color_all