from app.db.database import SessionLocal
from app.models.schemas.permission import PermissionUpdate
from app.db.tables import Permission


db = SessionLocal()


def update_permission(permission_in: PermissionUpdate):
    
    db.query(Permission).\
    filter(Permission.id_permission == permission_in.id_permission).\
    update({Permission.name: permission_in.name})
    db.commit()
    db.close()
    return permission_in