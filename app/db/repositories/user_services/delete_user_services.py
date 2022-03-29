from sqlalchemy import false
from app.db.database import SessionLocal
from app.db.tables import UserServices


db = SessionLocal()


def delete_user_services(id_size: int):
    db.query(UserServices).filter(UserServices.id_user == id_size).delete()
    db.commit()