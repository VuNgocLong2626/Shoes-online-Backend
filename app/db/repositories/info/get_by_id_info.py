from sqlalchemy import false
from app.db.database import SessionLocal
from app.models.schemas.user import UserToken
from app.db.tables import Info


db = SessionLocal()


def get_by_id_info(id_info: int):
    respon = db.query(Info).filter(Info.id_info == id_info).first()
    db.close()
    return respon
