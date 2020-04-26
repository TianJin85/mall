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
        # 首次添加地址默认为True
        if data["default"] == "True":
            address = Address.query.filter_by(userId=data["userId"], delete_time=None, default=True).first()
            if address:
                address.update(
                    default=False,
                    commit=True

                )

            Address.create(
                userId=int(data["userId"]),
                userName=data["userName"],
                address=data["address"],
                phoneCode=data["phoneCode"],
                default=True,
                commit=True
            )
        else:
                Address.create(
                    userId=int(data["userId"]),
                    userName=data["userName"],
                    address=data["address"],
                    phoneCode=data["phoneCode"],
                    default=False,
                    commit=True
                )

    @classmethod
    def amend_default_address(cls, form):
        address = Address.query.filter_by(userId=form.userId.data, delete_time=None, default=True).first()
        if address:
            address.update(
                default=False,
                commit=True
            )
        else:
            raise NotFound(msg='没有找到相关用户')
        address = Address.query.filter_by(id=form.id.data, delete_time=None).first()

        if address:
            address.update(
                userName=form.userName.data,
                address=form.address.data,
                phoneCode=form.phoneCode.data,
                default=True,
                commit=True
            )
        else:
            raise NotFound(msg='没有找到相关地址')

    @classmethod
    def address_list(cls, userId):
        address = Address.query.filter_by(userId=userId, delete_time=None).all()
        if address:
            return address
        else:
            raise NotFound(msg="没有找到相关地址")

    @classmethod
    def delete_address(cls, id):
        address = Address.query.filter_by(id=id, delete_time=None).first()
        if address:
            address.delete(
                commit=True
            )
        else:
            raise NotFound(msg="没有找到相关地址")
