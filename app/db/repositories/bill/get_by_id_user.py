from sqlalchemy import false
from app.db.database import SessionLocal
from app.db.tables import Bill


db = SessionLocal()


def get_by_id_user(id_user: int):
    respon = db.query(Bill).filter(Bill.id_user== id_user).all()
    db.close()
    return respon