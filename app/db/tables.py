from sqlalchemy import (Boolean,
                        Column, Float,
                        Integer,
                        String,
                        ForeignKey,
                        DateTime,
                        null)
from app.db.database import Base
from sqlalchemy.orm import relationship


class Info(Base):
    __tablename__ = "info"

    id_info = Column(Integer, primary_key=True, index=True)

    phone = Column(String(12))
    full_name = Column(String(250))
    dob = Column(DateTime)
    email = Column(String(250))
    address = Column(String(250))

    user = relationship("User",
                        back_populates="info",
                        cascade="all, delete",
                        passive_deletes=True)


class Permission(Base):
    __tablename__ = "permission"

    id_permission = Column(Integer, primary_key=True)
    name = Column(String(250), unique=True)

    user = relationship("User",
                        back_populates="permission",
                        cascade="all, delete",
                        passive_deletes=True)

    # def __init__(self, name):
    #     self.name = name


class NameServices(Base):
    __tablename__ = "nameservices"

    id_name_services = Column(Integer, primary_key=True)
    name = Column(String(250), unique=True)

    services = relationship("Services",
                            back_populates="nameservices",
                            cascade="all, delete",
                            passive_deletes=True)


class Services(Base):
    __tablename__ = "services"

    id_services = Column(Integer, primary_key=True, index=True)
    id_verifier = Column(Integer, ForeignKey(
        'user.id_user', ondelete="CASCADE"), default=null)
    id_name_services = Column(Integer, ForeignKey(
        'nameservices.id_name_services', ondelete="CASCADE"))

    booking_date = Column(DateTime)
    date_create = Column(DateTime)
    status = Column(String(250), default="")

    user = relationship("User", back_populates="services")
    nameservices = relationship("NameServices", back_populates="services")
    userservices = relationship("UserServices",
                                back_populates="services",
                                cascade="all, delete",
                                passive_deletes=True)


class UserServices(Base):
    __tablename__ = "userservices"  # co the co loi

    id_services = Column(Integer, ForeignKey(
        'services.id_services', ondelete="CASCADE"), primary_key=True)
    id_user = Column(Integer, ForeignKey(
        'user.id_user', ondelete="CASCADE"), primary_key=True)

    services = relationship("Services", back_populates="userservices")
    user = relationship("User", back_populates="userservices")


##
class Bill(Base):
    __tablename__ = "bill"

    id_bill = Column(Integer, primary_key=True, index=True)
    id_user = Column(Integer, ForeignKey('user.id_user', ondelete="CASCADE"))
    id_verifier = Column(Integer, ForeignKey(
        'user.id_user', ondelete="CASCADE"), default=null)

    status = Column(String(250), default=null)
    date_create = Column(DateTime)
    total = Column(String(250))
    method = Column(String(250))

    user = relationship("User", back_populates="bill_create",
                        foreign_keys=[id_user])
    verifier = relationship(
        "User", back_populates="bill_verification", foreign_keys=[id_verifier])
    bill_details = relationship("BillDetails",
                                back_populates="bill",
                                cascade="all, delete",
                                passive_deletes=True)


class User(Base):
    __tablename__ = "user"

    id_user = Column(Integer, primary_key=True, index=True)
    id_info = Column(Integer, ForeignKey('info.id_info', ondelete="CASCADE"))
    id_permission = Column(Integer, ForeignKey('permission.id_permission', ondelete="CASCADE"))

    account = Column(String(250), unique=True)
    password = Column(String(250))

    comments = relationship("Comments", back_populates="user")
    info = relationship("Info", back_populates="user")
    permission = relationship("Permission", back_populates="user")
    bill_verification = relationship("Bill",
                                     back_populates="verifier",
                                     cascade="all, delete",
                                     passive_deletes=True,
                                     foreign_keys=[Bill.id_verifier])
    bill_create = relationship("Bill",
                               back_populates="user",
                               cascade="all, delete",
                               passive_deletes=True,
                               foreign_keys=[Bill.id_user])
    services = relationship("Services",
                            back_populates="user",
                            cascade="all, delete",
                            passive_deletes=True)
    userservices = relationship("UserServices",
                                back_populates="user",
                                cascade="all, delete",
                                passive_deletes=True)


class Comments(Base):
    __tablename__ = "comments"

    id_comments = Column(Integer, primary_key=True, index=True)
    id_user = Column(Integer, ForeignKey('user.id_user', ondelete="CASCADE"))
    Content = Column(String(250))
    Date = Column(DateTime)

    user = relationship("User", back_populates="comments")
    rate_product = relationship("RateProduct", back_populates="comments")


class Gender(Base):
    __tablename__ = "gender"

    id_gender = Column(Integer, primary_key=True, index=True)
    name = Column(String(250), unique=True)

    product = relationship("Product",
                           back_populates="gender",
                           cascade="all, delete",
                           passive_deletes=True)


class Promotion(Base):
    __tablename__ = "promotion"

    id_promotion = Column(Integer, primary_key=True, index=True)
    name = Column(String(250))
    detail = Column(String(250))
    reduction = Column(Integer)

    category = relationship("Category",
                            back_populates="promotion",
                            cascade="all, delete",
                            passive_deletes=True)


class Category(Base):
    __tablename__ = "category"

    id_category = Column(Integer, primary_key=True, index=True)
    id_promotion = Column(Integer, ForeignKey(
        'promotion.id_promotion', ondelete="CASCADE"), default=null)
    name = Column(String(250))

    promotion = relationship("Promotion", back_populates="category")
    product = relationship("Product",
                           back_populates="category",
                           cascade="all, delete",
                           passive_deletes=True)


class Product(Base):
    __tablename__ = "product"

    id_product = Column(Integer, primary_key=True, index=True)
    id_category = Column(Integer, ForeignKey(
        'category.id_category', ondelete="CASCADE"))
    id_gender = Column(Integer, ForeignKey(
        'gender.id_gender', ondelete="CASCADE"))

    # msp = Column(String(250), unique=True)
    name = Column(String(250))
    detail = Column(String(250))
    money = Column(Integer)

    category = relationship("Category", back_populates="product")
    gender = relationship("Gender", back_populates="product")
    bill_details = relationship("BillDetails",
                                back_populates="product",
                                cascade="all, delete",
                                passive_deletes=True)
    product_detail = relationship("ProductDetail",
                                  back_populates="product",
                                  cascade="all, delete",
                                  passive_deletes=True)
    rate_product = relationship("RateProduct",
                                back_populates="product",
                                cascade="all, delete",
                                passive_deletes=True)


class BillDetails(Base):
    __tablename__ = "bill_details"

    id_bill_detail = Column(Integer, primary_key=True, index=True)
    id_bill = Column(Integer, ForeignKey('bill.id_bill', ondelete="CASCADE"))
    id_product = Column(Integer, ForeignKey(
        'product.id_product', ondelete="CASCADE"))

    quantily = Column(Integer)
    current_price = Column(Integer)

    bill = relationship("Bill", back_populates="bill_details")
    product = relationship("Product", back_populates="bill_details")


class Size(Base):
    __tablename__ = "size"

    id_size = Column(Integer, primary_key=True, index=True)
    size_number = Column(Float)

    size_quantity = relationship("SizeQuantity",
                                  back_populates="size",
                                  cascade="all, delete",
                                  passive_deletes=True)


class Image(Base):
    __tablename__ = "image"

    id_image = Column(Integer, primary_key=True, index=True)
    id_product_detail = Column(Integer, ForeignKey(
    'product_detail.id_product_detail', ondelete="CASCADE"))

    path = Column(String(250))

    product_detail = relationship("ProductDetail", back_populates="image")
    


class Color(Base):
    __tablename__ = "color"

    id_color = Column(Integer, primary_key=True, index=True)
    hex = Column(String(250))

    product_detail = relationship("ProductDetail",
                                  back_populates="color",
                                  cascade="all, delete",
                                  passive_deletes=True)
                                  

class ProductDetail(Base):
    __tablename__ = "product_detail"

    id_product_detail = Column(Integer, primary_key=True, index=True)
    id_product = Column(Integer, ForeignKey(
        'product.id_product', ondelete="CASCADE"))
    id_color = Column(Integer, ForeignKey(
        'color.id_color', ondelete="CASCADE"))
        
    # id_size = Column(Integer, ForeignKey('size.id_size', ondelete="CASCADE"))

    # quantity_sold = Column(Integer)
    # quantity = Column(Integer)

    product = relationship("Product", back_populates="product_detail")
    color = relationship("Color", back_populates="product_detail")
    image = relationship("Image",
                        back_populates="product_detail",
                        cascade="all, delete",
                        passive_deletes=True)
    size_quantity = relationship("SizeQuantity",
                        back_populates="product_detail",
                        cascade="all, delete",
                        passive_deletes=True)
    # size = relationship("Size", back_populates="product_detail")


class Rate(Base):
    __tablename__ = "rate"

    id_rate = Column(Integer, primary_key=True, index=True)
    number_star = Column(Integer)

    rate_product = relationship("RateProduct",
                                back_populates="rate",
                                cascade="all, delete",
                                passive_deletes=True)


class RateProduct(Base):
    __tablename__ = "rate_product"

    id_rate_product = Column(Integer, primary_key=True, index=True)
    id_product = Column(Integer, ForeignKey(
        'product.id_product', ondelete="CASCADE"))
    id_rate = Column(Integer, ForeignKey('rate.id_rate', ondelete="CASCADE"))
    id_comments = Column(Integer, ForeignKey(
        'comments.id_comments', ondelete="CASCADE"))

    product = relationship("Product", back_populates="rate_product")
    rate = relationship("Rate", back_populates="rate_product")
    comments = relationship("Comments", back_populates="rate_product")


class SizeQuantity(Base):
    __tablename__ = "size_quantity"

    id_size_quantity = Column(Integer, primary_key=True, index=True)
    id_product_detail =  Column(Integer, ForeignKey(
        'product_detail.id_product_detail', ondelete="CASCADE"))
    id_size = Column(Integer, ForeignKey('size.id_size', ondelete="CASCADE"))

    quantity_sold = Column(Integer)
    quantity = Column(Integer)

    product_detail = relationship("ProductDetail", back_populates="size_quantity")
    size = relationship("Size", back_populates="size_quantity")