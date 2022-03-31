from sqlalchemy import false
from app.db.database import SessionLocal
from app.models.schemas.product import ProductCreate
from app.db.tables import Product, ProductDetail, Image, Color
from typing import List


db = SessionLocal()


def get_by_in_id_category_and_color(id_category: List[int], id_color: List[int]):
    db.close()
    respon = db.query(Product).join(ProductDetail).filter(Product.id_category.in_(id_category), ProductDetail.id_color.in_(id_color)).all()
    return respon