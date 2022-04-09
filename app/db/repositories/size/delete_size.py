from sqlalchemy import false
from app.db.database import SessionLocal
from app.db.tables import Size


db = SessionLocal()


def delete_size(id_size: int):
    db.query(Size).filter(Size.id_size == id_size).delete()
    db.commit()
    db.close()