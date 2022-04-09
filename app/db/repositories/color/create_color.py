from sqlalchemy import false
from app.db.database import SessionLocal
from app.models.schemas.product_detail import ColorCreate
from app.db.tables import Color


db = SessionLocal()


def create_color(color_in: ColorCreate):
    color_new = Color(**color_in.dict())
    db.add(color_new)
    try:
        db.flush()
        db.commit()
        return color_new
    except:    
        db.rollback()
        return None