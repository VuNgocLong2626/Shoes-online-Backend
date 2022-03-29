from app.db.database import SessionLocal
from app.db.tables import Services, UserServices
import sqlalchemy


db = SessionLocal()


def get_by_chua_join_user_services():
    db.close()
    respon = db.query(Services, UserServices).join(UserServices).filter(Services.status.like("%Chua%")).all()
    return respon