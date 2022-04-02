from sqlalchemy import false
from app.db.database import SessionLocal
from app.models.schemas.user import UserLogin
from app.db.tables import User, Info


db = SessionLocal()


def get_all_admin():
    db.close()
    respon = db.query(User.account, Info.full_name).join(Info).filter(User.id_permission.in_((1,2))).all()
    return respon