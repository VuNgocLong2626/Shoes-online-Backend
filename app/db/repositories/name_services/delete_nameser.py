from sqlalchemy import false
from app.db.database import SessionLocal
from app.models.schemas.name_services import NameServicesCreate
from app.db.tables import NameServices


db = SessionLocal()


def delete_nameser(id_nameser: int):
    db.query(NameServices).filter(NameServices.id_name_services == id_nameser).delete()
    db.commit()
    db.close()