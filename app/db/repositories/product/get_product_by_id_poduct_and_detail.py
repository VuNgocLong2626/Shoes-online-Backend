from sqlalchemy import false
from app.db.database import SessionLocal
from app.models.schemas.product import ProductCart
from app.db.tables import Product, ProductDetail, Image, Color
from typing import List


db = SessionLocal()


def get_product_by_id_poduct_and_detail(product_in: ProductCart):
    respon = db.query(Product.name, ProductDetail.id_product_detail, Image.path).join(Product).join(Image).filter(Product.id_product == product_in.id_product, ProductDetail.id_product_detail == product_in.id_product_detail).first()
    db.close()
    return respon