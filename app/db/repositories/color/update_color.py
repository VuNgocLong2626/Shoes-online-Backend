from sqlalchemy import false
from app.db.database import SessionLocal
from app.models.schemas.product_detail import ColorUpdate
from app.db.tables import Color


db = SessionLocal()


def update_color(color_in: ColorUpdate):
    try:
        db.query(Color)\
            .filter(Color.id_color == color_in.id_color)\
            .update({Color.hex: color_in.hex})
        db.commit()
        db.close()
        return color_in
    except:
        return None