from sqlalchemy import false
from app.db.database import SessionLocal
from app.db.tables import Color


db = SessionLocal()


def delete_color(id_color: int):
    db.query(Color).filter(Color.id_color == id_color).delete()
    db.commit()
    db.close()