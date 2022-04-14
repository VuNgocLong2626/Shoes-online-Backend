from app.models.schemas import rate_comment as _rate_comment_schemas
from fastapi import HTTPException, status

from app.db.repositories.comment.create_comment import create_comment
from app.db.repositories.rate_comment.get_comment_join_rate_comment \
    import get_comment_join_rate_comment
from app.db.repositories.rate_comment.update_comment import update_comment

from app.db.repositories.rate_comment.create_rate_comment \
    import create_rate_comment
from app.db.repositories.user.get_info_by_id_user import get_info_by_id_user


class RateCommentServices():

    def create_rate_comment(_in: _rate_comment_schemas.CommentRateInDB):
        comment_in = _rate_comment_schemas.CommentCreate(**_in.content.dict())
        respon_comment = create_comment(comment_in)
        rate_comment = {
            "id_product": _in.id_product,
            "id_rate": _in.id_rate,
            "id_comments": respon_comment.id_comments
        }
        rate_comment_in = _rate_comment_schemas.CommentRateCreate(
            **rate_comment)
        respon = create_rate_comment(rate_comment_in)
        return respon

    def get_comment_id_product(id_product: int):
        results = get_comment_join_rate_comment(id_product)
        respon = []
        for result in results:
            dict_re = {**dict(result)}
            user_info = get_info_by_id_user(result.Comments.id_user)
            dict_re.update({"Info": user_info})
            respon.append(dict_re)

        return respon

    def update_comment(comment_in: _rate_comment_schemas.CommentUpdate):
        respon = update_comment(comment_in)
        return respon


def get_rate_comment_exception():
    credentials_exception = HTTPException(
        detail="Not Found",
        status_code=status.HTTP_404_NOT_FOUND,
    )
    return credentials_exception


def get_rate_comment_done():
    credentials_exception = HTTPException(
        detail="Done",
        status_code=status.HTTP_200_OK
    )
    return credentials_exception


def get_rate_comment_create_exception():
    credentials_exception = HTTPException(
        detail="Not Create",
        status_code=status.HTTP_400_BAD_REQUEST,
    )
    return credentials_exception
