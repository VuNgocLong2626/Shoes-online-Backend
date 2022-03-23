from sqlalchemy import false
from app.db.database import SessionLocal
from app.db.tables import Bill


db = SessionLocal()


def get_by_id_user_and_bill(id_user: int, id_bill: int):
    db.close()
    respon = db.query(Bill).filter(Bill.id_user== id_user, Bill.id_bill==id_bill).first()
    return respon