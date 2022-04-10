from sqlalchemy import false
from app.db.database import SessionLocal
from app.models.schemas.product_detail import ImageUpdate
from app.db.tables import Image


db = SessionLocal()


def delete_all_image(id_product_detail: int):
    db.query(Image).filter(Image.id_product_detail == id_product_detail).delete()
    db.commit()
    db.close()