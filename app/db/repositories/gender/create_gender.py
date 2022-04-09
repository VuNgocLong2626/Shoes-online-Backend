from sqlalchemy import false
from app.db.database import SessionLocal
from app.models.schemas.gender import GenderCreate
from app.db.tables import Gender


db = SessionLocal()


def create_gender(gender_in: GenderCreate):
    gender_new = Gender(**gender_in.dict())
    db.add(gender_new)
    try:
        db.flush()
        db.commit()
        return gender_new
    except:    
        db.rollback()
        return None