from sqlalchemy import false
from app.db.database import SessionLocal
from app.models.schemas.product import ProductUpdateForm
from app.db.tables import Product


db = SessionLocal()


def update_product_basic(product_in: ProductUpdateForm):
    try:
        db.query(Product).\
        filter(Product.id_product == product_in.id_product).\
        update({
            Product.name: product_in.name,
            Product.detail: product_in.detail,
            Product.money: product_in.money,
            Product.id_gender: product_in.id_gender,
            Product.id_category: product_in.id_category
            })
        db.commit()
        db.close()
        return product_in
    except:
        return None