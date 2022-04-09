from sqlalchemy import false
from app.db.database import SessionLocal
from app.models.schemas.product import ProductCreate
from app.db.tables import Product, ProductDetail, Image, Color
from typing import List


db = SessionLocal()


def get_by_in_id_color(id_color: List[int]):
    respon = db.query(Product).join(ProductDetail).filter(ProductDetail.id_color.in_(id_color)).all()
    db.close()
    return respon