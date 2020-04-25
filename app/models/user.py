# -*- encoding: utf-8 -*-
"""
@File    : user.py
@Time    :  2020/4/22 14:14
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
from lin.exception import NotFound, ParameterException, Failed
from lin.interface import InfoCrud as Base
from sqlalchemy import Column, String, Integer, Float, Boolean, ForeignKey
from werkzeug.security import generate_password_hash, check_password_hash

from app.exception.exception import Success


class UserInfo(Base):
    __tablename__ = "UserInfo"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nickName = Column("nickName", String(32), nullable=False, unique=True, comment="用户呢称")
    _passWord = Column("passWord", String(100), nullable=False, comment="用户密码")
    phoneCode = Column("phoneCode", String(11), nullable=False, unique=True, comment="电号号码")
    headPortrait = Column("headPortrait", String(120), nullable=False,
                          default=r"/2020/04/23/119e952e-8546-11ea-ada4-3ca0670be558.jpg", comment="头像")

    @property
    def password(self):
        return self._passWord

    @password.setter
    def password(self, raw):
        self._passWord = generate_password_hash(raw)

    def check_password(self, raw):
        return check_password_hash(self._passWord, raw)

    @classmethod
    def register_user(cls, form):
        nickName = UserInfo.query.filter_by(nickName=form.nickName.data).first()
        if nickName:
            raise Failed("名称以被使用")

        phoneCode = UserInfo.query.filter_by(phoneCode=form.phoneCode.data).first()

        if phoneCode:
            raise Failed("用户以注册")

        user = UserInfo()
        user.password = form.passWord.data
        UserInfo.create(
            nickName=form.nickName.data,
            _passWord=user._passWord,
            phoneCode=form.phoneCode.data,
            commit=True
        )

    @classmethod
    def amend(cls, user):

        pass


# class Collect(Base):
#     __tablename__ = "Collect"
#
#     id = Column("id", Integer, primary_key=True, autoincrement=True)
#     userId = Column("userId", Integer, ForeignKey("UserInfo.id"), nullable=False, comment="用户id")
#     commId = Column("commId", Integer, nullable=False, comment="商品id")
#
#
# class Footprint(Base):
#     __tablename__ = "Footprint"
#
#     id = Column("id", Integer, primary_key=True, autoincrement=True)
#     userId = Column("userId", Integer, ForeignKey("UserInfo.id"), nullable=True, comment="用户id")
#     commId = Column("commId", Integer, nullable=True, comment="商品id")
#
#
# class Address(Base):
#     __tablename__ = "Address"
#
#     id = Column("id",Integer, primary_key=True, autoincrement=True, comment="收货地址id")
#     userId = Column("userId", Integer, ForeignKey("UserInfo.id"), nullable=False, comment="用户id")
#     userName = Column("userName", String(32), nullable=False, comment="用户姓名")
#     address = Column("address", String(250), nullable=False, comment="收货地址")
#     phoneCode = Column("phoneCode", String(11), nullable=False, comment="电话号码")
#     default = Column("default", Boolean(), nullable=False, comment="默认地址")


