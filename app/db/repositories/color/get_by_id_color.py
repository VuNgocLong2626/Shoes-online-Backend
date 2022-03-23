from sqlalchemy import false
from app.db.database import SessionLocal
from app.models.schemas.product_detail import ColorCreate
from app.db.tables import Color


db = SessionLocal()


def get_by_id_color(id_color: int):
    db.close()
    respon = db.query(Color).filter(Color.id_color == id_color).first()
    return respon
