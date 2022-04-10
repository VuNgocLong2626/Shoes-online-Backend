from sqlalchemy import false
from app.db.database import SessionLocal
from app.db.tables import Bill


db = SessionLocal()


def get_count_bill():
    respon = db.query(Bill).count()
    db.close()
    return respon