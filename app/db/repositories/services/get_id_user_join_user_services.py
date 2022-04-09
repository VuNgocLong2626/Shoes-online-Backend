from app.db.database import SessionLocal
from app.models.schemas.uesr_services import ServicesCreate
from app.db.tables import Services, UserServices
import sqlalchemy


db = SessionLocal()


def get_by_id_user_join_user_services(id_user: int):
    respon = db.query(Services, UserServices).join(UserServices).filter(UserServices.id_user == id_user).all()
    db.close()
    return respon