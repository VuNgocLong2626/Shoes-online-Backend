from sqlalchemy import false
from app.db.database import SessionLocal
from app.models.schemas.product import ProductCreate
from app.db.tables import Product


db = SessionLocal()


def get_by_name(name: int):
    respon = db.query(Product).filter(Product.name == name).first()
    db.close()
    return respon