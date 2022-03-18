from sqlalchemy import false
from app.db.database import SessionLocal
from app.models.schemas.product import ProductCreate
from app.db.tables import Product


db = SessionLocal()


def get_by_name(name: int):
    db.close()
    respon = db.query(Product).filter(Product.id_product == name).first()
    return respon