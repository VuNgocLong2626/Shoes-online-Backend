from sqlalchemy import false
from app.db.database import SessionLocal
from app.db.tables import BillDetails


db = SessionLocal()


def get_bill_detail_by_id_bill(id_bill: int):
    db.close()
    respon = db.query(BillDetails).filter(BillDetails.id_bill== id_bill).all()
    return respon