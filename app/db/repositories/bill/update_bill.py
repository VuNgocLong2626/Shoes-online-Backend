from sqlalchemy import false
from app.db.database import SessionLocal
from app.models.schemas.bill import BillUpdate
from app.db.tables import Bill


db = SessionLocal()


def update_bill(bill_in: BillUpdate):
    try:
        db.query(Bill).\
        filter(Bill.id_bill == bill_in.id_bill ).\
        update({
            Bill.id_verifier: bill_in.id_verifier,
            Bill.status: bill_in.status
                })
        db.commit()
        return bill_in
    except:
        return None