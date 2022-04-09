from sqlalchemy import false
from app.db.database import SessionLocal
from app.models.schemas.size_quatity import SizeQuantityCreate
from app.db.tables import SizeQuantity, Size


db = SessionLocal()


def get_quantity_by_id_size_quantity(id_size_quantity: int):
    respon = db.query(SizeQuantity, Size).join(Size).filter(SizeQuantity.id_size_quantity == id_size_quantity).first()
    db.close()
    return respon