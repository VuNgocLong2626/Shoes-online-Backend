from sqlalchemy import false
from app.db.database import SessionLocal
from app.models.schemas.product_detail import ProductDetailCreate
from app.db.tables import ProductDetail


db = SessionLocal()


def get_by_id_product_detail(id_product: int):
    respon = db.query(ProductDetail).filter(ProductDetail.id_product ==  id_product).all()
    db.close()
    return respon