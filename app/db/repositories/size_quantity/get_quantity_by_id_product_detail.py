from sqlalchemy import false
from app.db.database import SessionLocal
from app.models.schemas.size_quatity import SizeQuantityCreate
from app.db.tables import SizeQuantity, Size


db = SessionLocal()


def get_quantity_by_id_product_detail(id_product_detail: int):
    db.close()
    respon = db.query(SizeQuantity, Size.size_number).join(Size).filter(SizeQuantity.id_product_detail == id_product_detail).all()
    return respon