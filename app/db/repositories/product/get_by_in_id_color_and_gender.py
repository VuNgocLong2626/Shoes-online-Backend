from sqlalchemy import false
from app.db.database import SessionLocal
from app.models.schemas.product import ProductCreate
from app.db.tables import Product, ProductDetail, Image, Color
from typing import List


db = SessionLocal()


def get_by_in_id_color_and_gender(id_color: List[int], id_gender):
    respon = db.query(Product).join(ProductDetail).filter(ProductDetail.id_color.in_(id_color), Product.id_gender == id_gender).all()
    db.close()
    return respon