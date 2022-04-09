from ast import In
from sqlalchemy import false
from app.db.database import SessionLocal
from app.models.schemas.user import UserToken
from app.models.schemas.info import InfoUpdate
from app.db.tables import Info


db = SessionLocal()


def update_info(user: UserToken, info_in: InfoUpdate):
    try:
        db.query(Info).\
        filter(Info.id_info == user.id_info).\
        update({Info.full_name: info_in.full_name,
                Info.email: info_in.email,
                Info.dob: info_in.dob,
                Info.phone: info_in.phone
                })
        db.commit()
        db.close()
        return info_in
    except:
        db.close()
        return None