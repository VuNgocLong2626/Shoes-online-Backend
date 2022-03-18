from sqlalchemy import false
from app.db.database import SessionLocal
from app.models.schemas.product import ProductCreate
from app.db.tables import Product


db = SessionLocal()


def get_all_product_basic():
    db.commit()
    respon = db.query(Product).all()
    return respon