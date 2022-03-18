from sqlalchemy import false
from app.db.database import SessionLocal
from app.models.schemas.product import ProductCreateForm
from app.db.tables import Product


db = SessionLocal()


def create_product(product_in: ProductCreateForm):
    product_new = Product(**product_in.dict())
    db.add(product_new)
    try:
        db.flush()
        db.commit()
        return product_new
    except:    
        return None