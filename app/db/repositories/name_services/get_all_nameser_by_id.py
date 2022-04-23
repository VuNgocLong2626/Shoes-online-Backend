from app.db.database import SessionLocal
from app.db.tables import NameServices


db = SessionLocal()


def get_all_nameser_by_id(id_service: int):
    nameser_all = db.query(NameServices).filter(NameServices.id_name_services == id_service).first()
    db.close()
    return nameser_all
