from sqlalchemy import false
from app.db.database import SessionLocal
from app.models.schemas.billdetail import BillDetailCreate
from app.db.tables import BillDetails
import sqlalchemy


db = SessionLocal()


def create_bill_detail(bill_detail_in: BillDetailCreate):
    bill_new = BillDetails(**bill_detail_in.dict())
    db.add(bill_new)
    try:
        db.flush()
        db.commit()
        return bill_new
    except:
        db.rollback() 
        return None