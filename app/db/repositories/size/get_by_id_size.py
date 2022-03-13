from sqlalchemy import false
from app.db.database import SessionLocal
from app.models.schemas.product_detail import ColorCreate
from app.db.tables import Size


db = SessionLocal()


def get_by_id_size(id_size: int):
    db.commit()
    respon = db.query(Size).filter(Size.id_size == id_size).first()
    return respon
