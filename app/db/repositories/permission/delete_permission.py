from app.db.database import SessionLocal
from app.models.schemas.permission import PermissionCreate
from app.db.tables import Permission


db = SessionLocal()


def delete_permission(id_permission):
    db.query(Permission).filter(Permission.id_permission == id_permission).delete()
    db.commit()
    