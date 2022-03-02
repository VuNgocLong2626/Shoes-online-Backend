from app.db.database import SessionLocal
from app.models.schemas.permission import PermissionCreate
from app.db.tables import Permission


db = SessionLocal()


def get_all():
    permissions = db.query(Permission).all()
    return permissions