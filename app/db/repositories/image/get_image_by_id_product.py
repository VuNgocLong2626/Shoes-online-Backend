from sqlalchemy import false
from app.db.database import SessionLocal
from app.models.schemas.product_detail import ImageOutDB
from app.db.tables import Image


db = SessionLocal()


def get_image_by_id_product(id_product_detail: int):
    # respon = db.query(Image.path).filter(Image.id_product_detail == id_product_detail).all()
    # with_entities
    respon = db.query(Image).with_entities(Image.path).filter(Image.id_product_detail == id_product_detail).all()
    db.close()
    return respon