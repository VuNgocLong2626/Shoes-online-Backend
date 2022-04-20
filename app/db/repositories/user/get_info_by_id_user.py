from app.db.database import SessionLocal
from app.db.tables import User, Info


db = SessionLocal()


def get_info_by_id_user(id_user: int):
    respon = db.query(Info).join(User).filter(User.id_user == id_user).first()
    db.close()
    return respon
