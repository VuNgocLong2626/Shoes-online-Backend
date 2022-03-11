from sqlalchemy import false
from app.db.database import SessionLocal
from app.models.schemas.user import UserChangePassword, UserToken
from app.db.tables import User


db = SessionLocal()


def update_password(user_in: UserToken, passw: str):
    try:
        db.query(User).\
            filter(User.id_user == user_in.id_user).\
            update({User.password: passw})
        db.commit()
        return True
    except:
        return None