from sqlalchemy import false
from app.db.database import SessionLocal
from app.models.schemas.info import InfoCreate
from app.db.tables import User, Info


db = SessionLocal()


def create_info(info_in: InfoCreate):
    new_info = Info(**info_in.dict())
    db.add(new_info)
    try:
        db.flush()
        db.commit()
        return new_info
    except:
        db.rollback()
        return false