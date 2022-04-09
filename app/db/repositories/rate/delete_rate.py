from sqlalchemy import false
from app.db.database import SessionLocal
from app.models.schemas.rate import RateUpdate
from app.db.tables import Rate


db = SessionLocal()


def delete_rate(id_rate: int):
    db.query(Rate).filter(Rate.id_rate == id_rate).delete()
    db.commit()
    db.close()
    return id_rate