from sqlalchemy import false
from app.db.database import SessionLocal
from app.models.schemas.bill import BillCreate,BillDetail
from app.db.tables import Bill
import sqlalchemy


db = SessionLocal()


def create_bill(bill_in: BillCreate):
    bill_new = Bill(**bill_in.dict(),id_verifier=sqlalchemy.sql.null())
    db.add(bill_new)
    try:
        db.flush()
        db.commit()
        return bill_new
    except:    
        return None