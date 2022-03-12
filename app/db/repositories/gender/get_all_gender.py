from sqlalchemy import false
from app.db.database import SessionLocal
from app.models.schemas.gender import GenderCreate
from app.db.tables import Gender


db = SessionLocal()


def get_all_gender():
    db.commit()
    respon = db.query(Gender).all()
    return respon