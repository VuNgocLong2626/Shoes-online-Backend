from app.db.database import SessionLocal
from app.models.schemas.permission import PermissionCreate
from app.db.tables import Permission


db = SessionLocal()


def get_by_id_permission(id: int):
    permissions = db.query(Permission).filter(Permission.id_permission == id).first()
    return permissions