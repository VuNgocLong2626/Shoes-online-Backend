from sqlalchemy import false
from app.db.database import SessionLocal
from app.models.schemas.product import ProductCreate
from app.db.tables import Product
from typing import List


db = SessionLocal()


def get_product_by_name(name: str):
    respon = db.query(Product).filter(Product.name.like(f"%{name}%")).all()
    db.close()
    return respon