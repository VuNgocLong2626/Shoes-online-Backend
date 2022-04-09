from sqlalchemy import false
from app.db.database import SessionLocal
from app.models.schemas.rate_comment import CommentUpdate
from app.db.tables import Comments


db = SessionLocal()


def update_comment(comment_in: CommentUpdate):
    try:
        db.query(Comments)\
            .filter(Comments.id_comments == comment_in.id_comments)\
            .update({
                Comments.Content: comment_in.Content,
                Comments.Date: comment_in.Date
                    })
        db.commit()
        db.close()
        return comment_in
    except:
        return None