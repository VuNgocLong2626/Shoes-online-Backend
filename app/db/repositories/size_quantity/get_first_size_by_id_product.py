from sqlalchemy import false
from app.db.database import SessionLocal
from app.db.tables import SizeQuantity


db = SessionLocal()


def get_first_size_by_id_product(id_product_detail: int):
    respon = db.query(SizeQuantity).filter(SizeQuantity.id_product_detail == id_product_detail).first()
    db.close()
    return respon