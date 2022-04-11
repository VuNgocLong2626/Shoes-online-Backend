from typing import List
from sqlalchemy import false
from app.db.database import SessionLocal
from app.models.schemas.product import ProductCreate
from app.db.tables import Product


db = SessionLocal()


def get_by_list_id_category(id_category: List[int]):
    respon = db.query(Product).filter(Product.id_category.in_(id_category)).all()
    db.close()
    return respon