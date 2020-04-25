# -*- encoding: utf-8 -*-
"""
@File    : product.py
@Time    :  2020/4/24 13:49
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
from unittest.mock import Base

from sqlalchemy import Column, Integer, ForeignKey, Float, String


class ProductModel(Base):

    __tablename__ = "ProductModel"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    commId = Column("commId", Integer, ForeignKey("Commodity.id"), nullable=False, comment="商品id")
    price = Column("price", Float, nullable=False, comment="商品价格")
    productModel = Column('productModel', String(250), nullable=False, comment="商品型号")