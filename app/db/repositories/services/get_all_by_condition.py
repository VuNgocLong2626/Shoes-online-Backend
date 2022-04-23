from app.db.database import SessionLocal
from app.db.tables import Services, UserServices


db = SessionLocal()


def get_all_by_condition(condition: int):
    respon = db.query(Services, UserServices).join(UserServices)\
        .filter(Services.status.like(f"%{condition}%")).all()
    db.close()
    return respon
