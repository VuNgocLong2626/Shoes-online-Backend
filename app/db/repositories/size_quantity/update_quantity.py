from sqlalchemy import false
from app.db.database import SessionLocal
from app.models.schemas.size_quatity import SizeQuantityUpdate
from app.db.tables import SizeQuantity


db = SessionLocal()


def update_quantity(quantity_in: SizeQuantityUpdate):
    try:
        db.query(SizeQuantity).\
        filter(SizeQuantity.id_size_quantity == quantity_in.id_size_quantity).\
        update({
            SizeQuantity.id_product_detail: quantity_in.id_product_detail,
            SizeQuantity.id_size: quantity_in.id_size,
            SizeQuantity.quantity: quantity_in.quantity,
            SizeQuantity.quantity_sold: quantity_in.quantity_sold
            })
        db.commit()
        db.close()
        return quantity_in
    except:
        return None