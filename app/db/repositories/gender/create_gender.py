from sqlalchemy import false
from app.db.database import SessionLocal
from app.models.schemas.gender import GenderCreate
from app.db.tables import Gender
from typing import Optional


db = SessionLocal()


def create_gender(gender_in: Optional[GenderCreate] = None, name: Optional[str] = None):
    if name is None:
        gender_new = Gender(**gender_in.dict())
    else:
        gender_new = Gender(name=name)
    db.add(gender_new)
    try:
        db.flush()
        db.commit()
        return gender_new
    except:    
        db.rollback()
        return None