from sqlalchemy import false
from app.db.database import SessionLocal
from app.models.schemas.gender import GenderUpdate
from app.db.tables import Gender


db = SessionLocal()


def update_gender(gender_in: GenderUpdate):
    try:
        db.query(Gender).\
        filter(Gender.id_gender == gender_in.id_gender).\
        update({Gender.name: gender_in.name
                })
        db.commit()
        db.close()
        return gender_in
    except:
        return None