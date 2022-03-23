from sqlalchemy import false
from app.db.database import SessionLocal
from app.models.schemas.name_services import NameServicesCreate
from app.db.tables import NameServices


db = SessionLocal()


def get_all_nameser():
    db.close()
    nameser_all = db.query(NameServices).all()
    return nameser_all