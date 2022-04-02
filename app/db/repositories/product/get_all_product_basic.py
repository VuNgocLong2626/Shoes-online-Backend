from sqlalchemy import false
from app.db.database import SessionLocal
from app.models.schemas.product import ProductCreate
from typing import List, Optional
from app.db.tables import Product, Gender


db = SessionLocal()


def get_all_product_basic(_gender: Optional[str] = None):
    db.close()
    if _gender is None:
        respon = db.query(Product).all()
    else:
        respon = db.query(Product).join(Gender).filter(Gender.name == _gender).all()
    return respon