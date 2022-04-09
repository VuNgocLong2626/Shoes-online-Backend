from sqlalchemy import false
from app.db.database import SessionLocal
from app.models.schemas.gender import GenderCreate
from app.db.tables import Gender


db = SessionLocal()


def get_by_id_gender(id_gender: int):
    respon = db.query(Gender).filter(Gender.id_gender == id_gender).first()
    db.close()
    return respon