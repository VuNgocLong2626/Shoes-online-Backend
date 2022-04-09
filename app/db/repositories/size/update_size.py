from sqlalchemy import false
from app.db.database import SessionLocal
from app.models.schemas.product_detail import SizeUpdate
from app.db.tables import Size


db = SessionLocal()


def update_size(size_in: SizeUpdate):
    try:
        db.query(Size)\
            .filter(Size.id_size == size_in.id_size)\
            .update({Size.size_number: size_in.size_number})
        db.commit()
        db.close()
        return size_in
    except:
        return None