# -*- encoding: utf-8 -*-
"""
@File    : order.py
@Time    :  2020/4/24 13:53
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
from lin.interface import InfoCrud as Base
from sqlalchemy import Column, Integer, ForeignKey, Float, Boolean


class Order(Base):
    __tablename__ = "Order"

    id = Column("id", Integer, primary_key=True, autoincrement=True, comment="订单id")
    commId = Column("commId", Integer, ForeignKey("Commodity.id"), nullable=False, comment="商品id")
    money = Column("money", Float, nullable=False, comment="商品金额")
    payment = Column("payment", Boolean, nullable=False, comment="是否支付")
    receiving = Column("receiving", Boolean, nullable=False, comment="是否收货")
    refund = Column("refund", Boolean, nullable=False, comment="是否退款")
    conut = Column("count", Integer, nullable=False, comment="商品数量")