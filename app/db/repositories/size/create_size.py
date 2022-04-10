from sqlalchemy import false
from app.db.database import SessionLocal
from app.models.schemas.product_detail import SizeCreate
from app.db.tables import Size
from typing import Optional


db = SessionLocal()


def create_size(size_in: Optional[SizeCreate] = None, number: Optional[int] = None):
    if number is None:
        size_new = Size(**size_in.dict())
    else:
        size_new = Size(size_number=number)
    db.add(size_new)
    try:
        db.flush()
        db.commit()
        return size_new
    except:    
        db.rollback()
        return false