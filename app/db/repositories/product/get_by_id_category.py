from sqlalchemy import false
from app.db.database import SessionLocal
from app.models.schemas.product import ProductCreate
from app.db.tables import Product


db = SessionLocal()


def get_by_id_category(id_category: int):
    respon = db.query(Product).filter(Product.id_category == id_category).all()
    db.close()
    return respon