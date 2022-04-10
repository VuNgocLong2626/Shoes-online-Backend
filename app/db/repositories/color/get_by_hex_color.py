from sqlalchemy import false
from app.db.database import SessionLocal
from app.db.tables import Color


db = SessionLocal()


def get_by_hex_color(name: str):
    color_all = db.query(Color).filter(Color.hex == name).first()
    db.close()
    return color_all