from sqlalchemy import false
from app.db.database import SessionLocal
from app.models.schemas.user import UserLogin
from app.db.tables import User, Info, Permission


db = SessionLocal()


def get_all_admin():
    respon = db.query(User.account, Info.full_name, Permission.name).join(Info).join(Permission).filter(User.id_permission.in_((1,2))).all()
    db.close()
    return respon