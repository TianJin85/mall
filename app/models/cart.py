# -*- encoding: utf-8 -*-
"""
@File    : cart.py
@Time    :  2020/4/24 13:55
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
from lin.exception import NotFound, ParameterException
from lin.interface import InfoCrud as Base
from sqlalchemy import Integer, Column, ForeignKey


class ShoppingCart(Base):
    __tablename__ = "ShoppingCart"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    commId = Column("commId", Integer, ForeignKey("Commodity.id"), nullable=False, comment="商品id")
    conut = Column("conut", Integer, comment="商品数量")