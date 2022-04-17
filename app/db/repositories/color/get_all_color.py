from app.db.database import SessionLocal
from app.db.tables import Color


db = SessionLocal()


def get_all_color():
    color_all = db.query(Color).all()
    db.close()
    return color_all
