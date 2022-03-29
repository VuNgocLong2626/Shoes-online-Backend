from app.db.database import SessionLocal
from app.models.schemas.uesr_services import ServicesCreate
from app.db.tables import Services
import sqlalchemy


db = SessionLocal()


def create_services(_in: ServicesCreate):
    services_new = Services(**_in.dict(), id_verifier=sqlalchemy.sql.null())
    db.add(services_new)
    try:
        db.flush()
        db.commit()
        return services_new
    except:    
        return None