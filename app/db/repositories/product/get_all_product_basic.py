from sqlalchemy import false
from app.db.database import SessionLocal
from app.models.schemas.product import ProductCreate
from typing import List, Optional
from app.db.tables import Product, Gender


db = SessionLocal()


def get_all_product_basic(id_gender: Optional[int] = None):
    if id_gender is None:
        respon = db.query(Product).all()
    else:
        respon = db.query(Product).join(Gender).filter(Gender.id_gender == id_gender).all()
    db.close()
    return respon