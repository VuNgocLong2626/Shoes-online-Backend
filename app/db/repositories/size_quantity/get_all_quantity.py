from sqlalchemy import false
from app.db.database import SessionLocal
from app.models.schemas.size_quatity import SizeQuantityCreate
from app.db.tables import SizeQuantity


db = SessionLocal()


def get_all_quantity():
    respon = db.query(SizeQuantity).all()
    db.close()
    return respon