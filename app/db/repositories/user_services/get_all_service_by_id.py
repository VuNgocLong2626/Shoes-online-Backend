from app.db.database import SessionLocal
from app.db.tables import UserServices, Services, NameServices


db = SessionLocal()


def get_all_service_by_id(id_user: int):
    respon = db.query(UserServices, Services)\
        .join(Services)\
        .filter(UserServices.id_user == id_user).all()
    db.close()
    return respon
