from sqlalchemy import false
from app.db.database import SessionLocal
from app.models.schemas.user import UserLogin
from app.db.tables import User, Info


db = SessionLocal()


def get_user(user_in: UserLogin):
    respon = db.query(User).filter(User.account == user_in.account).first()
    return respon
    # if respon:
    #     return respon
    # else:
    #     return false