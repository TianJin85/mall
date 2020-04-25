# -*- encoding: utf-8 -*-
"""
@File    : collect.py
@Time    :  2020/4/24 13:56
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
from lin.exception import NotFound, ParameterException
from lin.interface import InfoCrud as Base
from sqlalchemy import Integer, Column, ForeignKey


class Collect(Base):
    __tablename__ = "Collect"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    userId = Column("userId", Integer, ForeignKey("UserInfo.id"), nullable=False, comment="用户id")
    commId = Column("commId", Integer, nullable=False, comment="商品id")