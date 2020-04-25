# -*- encoding: utf-8 -*-
"""
@File    : address.py
@Time    :  2020/4/24 13:57
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
from lin.exception import NotFound, ParameterException
from lin.interface import InfoCrud as Base
from sqlalchemy import Integer, Column, ForeignKey, String, Boolean


class Address(Base):
    __tablename__ = "Address"

    id = Column("id",Integer, primary_key=True, autoincrement=True, comment="收货地址id")
    userId = Column("userId", Integer, ForeignKey("UserInfo.id"), nullable=False, comment="用户id")
    userName = Column("userName", String(32), nullable=False, comment="用户姓名")
    address = Column("address", String(250), nullable=False, comment="收货地址")
    phoneCode = Column("phoneCode", String(11), nullable=False, comment="电话号码")
    default = Column("default", Boolean, nullable=False, comment="默认地址")

    @classmethod
    def append(cls, data):

        Address.create(
            userId=data["userId"],
            userName=data["userName"],

        )