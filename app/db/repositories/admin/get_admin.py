from sqlalchemy import false
from app.db.database import SessionLocal
from app.models.schemas.user import UserLogin
from app.db.tables import User


db = SessionLocal()


def get_admin(user_in: UserLogin):
    respon = db.query(User).filter(User.account == user_in.account).first()
    return respon