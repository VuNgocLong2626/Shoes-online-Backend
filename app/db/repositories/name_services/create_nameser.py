from sqlalchemy import false
from app.db.database import SessionLocal
from app.models.schemas.name_services import NameServicesCreate
from app.db.tables import NameServices


db = SessionLocal()


def create_nameser(nameser_in: NameServicesCreate):
    nameser_new = NameServices(**nameser_in.dict())
    db.add(nameser_new)
    try:
        db.flush()
        db.commit()
        return nameser_new
    except:    
        return None