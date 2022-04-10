from sqlalchemy import false
from app.db.database import SessionLocal
from app.models.schemas.gender import GenderCreate
from app.db.tables import Gender


db = SessionLocal()


def get_gender_by_name(name: str):
    respon = db.query(Gender).filter(Gender.name == name).first()
    db.close()
    return respon