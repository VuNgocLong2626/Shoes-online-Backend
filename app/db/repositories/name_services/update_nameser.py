from sqlalchemy import false
from app.db.database import SessionLocal
from app.models.schemas.name_services import NameServicesUpdate
from app.db.tables import NameServices


db = SessionLocal()


def update_nameser(nameser_in: NameServicesUpdate):
    db.query(NameServices)\
        .filter(NameServices.id_name_services == nameser_in.id_name_services)\
        .update({NameServices.name: nameser_in.name})
    db.commit()

    return nameser_in