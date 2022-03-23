from sqlalchemy import false
from app.db.database import SessionLocal
from app.models.schemas.product_detail import ProductDetailCreate
from app.db.tables import ProductDetail,Image, Color


db = SessionLocal()


def get_all_john_image(id_product_detail: int):
    db.commit()
    respon = db.query(ProductDetail, Image, Color).join(Image).join(Color).filter(ProductDetail.id_product_detail == id_product_detail).first()
    return respon