from sqlalchemy import false
from app.db.database import SessionLocal
from app.models.schemas.product import ProductCreate
from typing import List, Optional
from app.db.tables import Product


db = SessionLocal()


def get_all_product_basic(id_gender: Optional[int] = None):
    db.close()
    if id_gender is None:
        respon = db.query(Product).all()
    else:
        respon = db.query(Product).filter(Product.id_gender == id_gender).all()
    return respon