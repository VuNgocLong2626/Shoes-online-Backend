from sqlalchemy import false
from app.db.database import SessionLocal
from app.models.schemas.user import UserCreate, UserInDB
from app.db.tables import User, Info


db = SessionLocal()


def create_user(user_in: UserInDB):
    new_user = User(**user_in.dict())
    db.add(new_user)
    try:
        db.flush()
        db.commit()
        return new_user
    except:
        db.rollback()    
        return false