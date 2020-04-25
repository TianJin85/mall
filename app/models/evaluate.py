# -*- encoding: utf-8 -*-
"""
@File    : evaluate.py
@Time    :  2020/4/24 13:52
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
from lin.interface import InfoCrud as Base
from sqlalchemy import Column, Integer, ForeignKey, String


class Evaluate(Base):
    __tablename__ = "Evaluate"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    commId = Column("commID", Integer, ForeignKey("Commodity.id"), nullable=False, comment="商品id")
    nickName = Column("nickName", String(32), nullable=False, comment="用户呢称")
    headPortrait = Column("headPortrait", String(250), nullable=False, comment="用户头像")
    content = Column("content", String(500), nullable=False, comment="评价内容")