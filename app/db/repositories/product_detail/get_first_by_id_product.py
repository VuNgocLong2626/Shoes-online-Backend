from sqlalchemy import false
from app.db.database import SessionLocal
from app.models.schemas.product_detail import ProductDetailCreate
from app.db.tables import ProductDetail


db = SessionLocal()


def get_first_by_id_product(id_product: int):
    respon = db.query(ProductDetail).filter(ProductDetail.id_product ==  id_product).first()
    db.close()
    return respon