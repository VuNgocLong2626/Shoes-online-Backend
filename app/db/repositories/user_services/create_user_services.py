from sqlalchemy import false
from app.db.database import SessionLocal
from app.models.schemas.uesr_services import UserServicesCreate
from app.db.tables import UserServices


db = SessionLocal()


def create_user_services(_in: UserServicesCreate):
    user_services_new = UserServices(**_in.dict())
    db.add(user_services_new)
    try:
        db.flush()
        db.commit()
        return user_services_new
    except:    
        db.rollback()
        return None