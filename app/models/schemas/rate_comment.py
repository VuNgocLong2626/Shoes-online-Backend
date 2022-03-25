from app.models.domain import (
                                base as _base,
                                comments as _comments_domain)


class CommentCreate(
    _base.UserId,
    _comments_domain.CommentsContent,
    _comments_domain.CommentsDate
):
    pass


class CommentDetail(
    _base.CommentsId,
    _base.UserId,
    _comments_domain.CommentsContent,
    _comments_domain.CommentsDate
):
    pass

    class Config:
        orm_mode = True


class CommentUpdate(    
    _base.CommentsId,
    _base.UserId,
    _comments_domain.CommentsContent,
    _comments_domain.CommentsDate
):
    pass


class CommentRateCreate(
    _base.ProductId,
    _base.RateId,
    _base.CommentsId
):
    pass


class CommentRateInDB(
    _base.ProductId,
    _base.RateId
):
    content: CommentCreate


class CommentRateDetail(
    _base.ProductId,
    _base.RateProductId,
    _base.RateId,
    _base.CommentsId
):
    pass

    class Config:
        orm_mode = True


class CommentRateUpdate(
    _base.ProductId,
    _base.RateProductId,
    _base.RateId,
    _base.CommentsId    
):
    pass