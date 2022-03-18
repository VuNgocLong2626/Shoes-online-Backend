from sqlalchemy import false
from app.db.database import SessionLocal
from app.models.schemas.product import ProductCreate
from app.db.tables import Product


db = SessionLocal()


def get_by_id_product(id_product: int):
    db.commit()
    respon = db.query(Product).filter(Product.id_product == id_product).first()
    return respon