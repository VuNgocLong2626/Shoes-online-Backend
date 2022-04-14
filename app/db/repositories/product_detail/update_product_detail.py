from app.db.database import SessionLocal
from app.models.schemas.product_detail import ProductDetailUpdate
from app.db.tables import ProductDetail


db = SessionLocal()


def update_product_detail(product_detail_in: ProductDetailUpdate):

    id_product_detail = product_detail_in.id_product_detail
    db.query(ProductDetail).\
        filter(
            ProductDetail.id_product_detail == id_product_detail
    ).update(
        {
            ProductDetail.id_color: product_detail_in.id_color
        }
    )
    db.commit()
    db.close()
    return product_detail_in
