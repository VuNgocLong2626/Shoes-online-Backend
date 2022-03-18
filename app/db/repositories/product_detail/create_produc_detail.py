from sqlalchemy import false
from app.db.database import SessionLocal
from app.models.schemas.product_detail import ProductDetailCreate
from app.db.tables import ProductDetail


db = SessionLocal()


def create_product_detail(product_in: ProductDetailCreate):
    product_new = ProductDetail(**product_in.dict())
    db.add(product_new)
    try:
        db.flush()
        db.commit()
        return product_new
    except:    
        return None