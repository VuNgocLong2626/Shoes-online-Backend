from sqlalchemy import false
from app.db.database import SessionLocal
from app.db.tables import Bill


db = SessionLocal()


def get_by_id_bill(id_bill: int):
    respon = db.query(Bill).filter(Bill.id_bill == id_bill).first()
    db.close()
    return respon