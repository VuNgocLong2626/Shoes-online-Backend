from sqlalchemy import false
from app.db.database import SessionLocal
from app.models.schemas.gender import GenderCreate
from app.db.tables import Gender


db = SessionLocal()


def delete_gender(id_gender: int):
    try:
        db.query(Gender).filter(Gender.id_gender == id_gender).delete()
        db.commit()
        db.close()
        return True
    except:
        db.close()
        return None