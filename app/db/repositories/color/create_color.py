from sqlalchemy import false
from app.db.database import SessionLocal
from app.models.schemas.product_detail import ColorCreate
from app.db.tables import Color
from typing import Optional


db = SessionLocal()


def create_color(color_in: Optional[ColorCreate] = None, name: Optional[str] = str):
    if name is None:
        color_new = Color(**color_in.dict())
    else:
        color_new = Color(hex=name)
    db.add(color_new)
    try:
        db.flush()
        db.commit()
        return color_new
    except:    
        db.rollback()
        return None