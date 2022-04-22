from app.db.database import SessionLocal
from app.db.tables import User


db = SessionLocal()


def get_user_by_account(account: str):
    respon = db.query(User).filter(User.account == account).first()
    db.close()
    return respon
