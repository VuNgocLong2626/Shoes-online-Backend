from sqlalchemy import false
from app.db.database import SessionLocal
from app.models.schemas.product_detail import ProductDetailCreate
from app.db.tables import ProductDetail


db = SessionLocal()


def get_all_product_detail():
    db.commit()
    respon = db.query(ProductDetail).all()
    return respon