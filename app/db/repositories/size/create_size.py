from sqlalchemy import false
from app.db.database import SessionLocal
from app.models.schemas.product_detail import SizeCreate
from app.db.tables import Size


db = SessionLocal()


def create_size(size_in: SizeCreate):
    size_new = Size(**size_in.dict())
    db.add(size_new)
    try:
        db.flush()
        db.commit()
        return size_new
    except:    
        return false