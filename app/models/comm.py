# -*- encoding: utf-8 -*-
"""
@File    : comm.py
@Time    :  2020/4/22 14:14
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
from lin.exception import NotFound, ParameterException
from lin.interface import InfoCrud as Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Boolean, Text, and_

from app.config.setting import BaseConfig


class Commodity(Base):
    __tablename__ = "Commodity"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    # linUserId = Column("linUserId", Integer, default=1, primary_key="UserInterface.id", comment="商家id")
    name = Column("name", String(23), nullable=False, comment="商品名称")
    salesVolum = Column("salesVolum", Integer, default=0, comment="商品销量")
    pepertory = Column("pepertory", Integer, nullable=False, comment="库存")
    titleImg = Column("titleImg", String(250), nullable=False, comment="商品标题图片")
    detailsImg = Column("detailsImg", Text, nullable=False, comment="商品详情")
    type = Column("type", String(32), nullable=False, comment="产品类型")
    product = Column("product", Text, nullable=False, comment="产品型号")

    @classmethod
    def insert_comm(cls, data):
        """
        添加商品
        :param form:
        :return:
        """
        Commodity.create(
            name=str(data["name"]),
            pepertory=int(data["pepertory"]),
            titleImg=str(data["titleImg"]),
            detailsImg=str(data["detailsImg"]),
            type=str(data["type"]),
            product=str(data["product"]),
            commit=True
        )

    @classmethod
    def update_comm(cls, data):
        """
        修改商品
        :param form:
        :return:
        """
        comm = Commodity.query.filter_by(id=data["id"], delete_time=None).first()
        if comm is None:
            raise NotFound(msg='没有找到相关商品')
        else:
            comm.update(
                name=str(data["name"]),
                pepertory=int(data["pepertory"]),
                titleImg=str(data["titleImg"]),
                detailsImg=str(data["detailsImg"]),
                type=str(data["type"]),
                product=str(data["product"]),
                commit=True
            )
            return True

    @classmethod
    def query_comm(cls, pageNumber):
        """
        分页数据
        :return: comm
        """

        comm = Commodity.get(start=(int(pageNumber)-1)*BaseConfig.COUNT_DEFAULT, count=BaseConfig.COUNT_DEFAULT, one=False, delete_time=None)

        return comm

    @classmethod
    def query_page_sum(cls):
        """
        获取总页数
        :return:
        """
        count = Commodity.query.filter_by(delete_time=None).count()

        return count

    @classmethod
    def del_comm(cls, id):
        comm = Commodity.query.filter_by(id=id, delete_time=None).first()
        if comm is None:
            return False
        else:
            comm.delete(
                commit=True
            )
            return True

    @classmethod
    def query_comm_details(cls, id):
        comm = Commodity.query.filter_by(id=id, delete_time=None).first()
        if comm is None:
            raise NotFound(msg='没有找到相关商品')
        else:
            return comm

    @classmethod
    def query_comm_lick(cls, name):
        name = "%"+name+"%"

        comm = Commodity.query.filter(Commodity.name.like(name)).all()
        return comm

    @classmethod
    def query_comm_type(cls, _type):
        comm = Commodity.query.filter_by(type=_type, delete_time=None).all()

        return comm


# class ProductModel(Base):
#
#     __tablename__ = "ProductModel"
#
#     id = Column("id", Integer, primary_key=True, autoincrement=True)
#     commId = Column("commId", Integer, ForeignKey("Commodity.id"), nullable=False, comment="商品id")
#     price = Column("price", Float, nullable=False, comment="商品价格")
#     productModel = Column('productModel', String(250), nullable=False, comment="商品型号")
#
#
# class Evaluate(Base):
#     __tablename__ = "Evaluate"
#
#     id = Column("id", Integer, primary_key=True, autoincrement=True)
#     commId = Column("commID", Integer, ForeignKey("Commodity.id"), nullable=False, comment="商品id")
#     nickName = Column("nickName", String(32), nullable=False, comment="用户呢称")
#     headPortrait = Column("headPortrait", String(250), nullable=False, comment="用户头像")
#     content = Column("content", String(500), nullable=False, comment="评价内容")
#
#
# class Order(Base):
#     __tablename__ = "Order"
#
#     id = Column("id", Integer, primary_key=True, autoincrement=True, comment="订单id")
#     commId = Column("commId", Integer, ForeignKey("Commodity.id"), nullable=False, comment="商品id")
#     money = Column("money", Float, nullable=False, comment="商品金额")
#     payment = Column("payment", Boolean, nullable=False, comment="是否支付")
#     receiving = Column("receiving", Boolean, nullable=False, comment="是否收货")
#     refund = Column("refund", Boolean, nullable=False, comment="是否退款")
#     conut = Column("count", Integer, nullable=False, comment="商品数量")
#
#
# class ShoppingCart(Base):
#     __tablename__ = "ShoppingCart"
#
#     id = Column("id", Integer, primary_key=True, autoincrement=True)
#     commId = Column("commId", Integer, ForeignKey("Commodity.id"), nullable=False, comment="商品id")
#     conut = Column("conut", Integer, comment="商品数量")