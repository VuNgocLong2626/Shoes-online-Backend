from sqlalchemy import false
from app.db.database import SessionLocal
from app.models.schemas.rate_comment import CommentCreate
from app.db.tables import Comments


db = SessionLocal()


def create_comment(comment_in: CommentCreate):
    comment_new = Comments(**comment_in.dict())
    db.add(comment_new)
    try:
        db.flush()
        db.commit()
        return comment_new
    except:    
        db.rollback()
        return None