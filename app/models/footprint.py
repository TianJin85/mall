# -*- encoding: utf-8 -*-
"""
@File    : footprint.py
@Time    :  2020/4/24 13:57
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
from lin.exception import NotFound, ParameterException
from lin.interface import InfoCrud as Base
from sqlalchemy import Integer, Column, ForeignKey

class Footprint(Base):
    __tablename__ = "Footprint"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    userId = Column("userId", Integer, ForeignKey("UserInfo.id"), nullable=True, comment="用户id")
    commId = Column("commId", Integer, nullable=True, comment="商品id")