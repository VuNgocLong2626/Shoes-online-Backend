from sqlalchemy import false
from app.db.database import SessionLocal
from app.db.tables import Bill


db = SessionLocal()


def get_bill_all():
    respon = db.query(Bill).all()
    db.close()
    return respon