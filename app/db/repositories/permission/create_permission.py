from sqlalchemy import false
from app.db.database import SessionLocal
from app.models.schemas.permission import PermissionCreate
from app.db.tables import Permission


db = SessionLocal()

def create_permission(permission_in: PermissionCreate):
    new_permisson = Permission(**permission_in.dict())
    db.add(new_permisson)
    try:
        db.flush()
        db.commit()
        return new_permisson
    except:
        db.rollback()
        return false