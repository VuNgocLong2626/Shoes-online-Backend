from sqlalchemy import false
from app.db.database import SessionLocal
from app.models.schemas.size_quatity import SizeQuantityCreate
from app.db.tables import SizeQuantity


db = SessionLocal()


def create_size_quatity(size_quatity_in: SizeQuantityCreate):
    size_quatity_new = SizeQuantity(**size_quatity_in.dict())
    db.add(size_quatity_new)
    try:
        db.flush()
        db.commit()
        return size_quatity_new
    except:    
        db.rollback()
        return None