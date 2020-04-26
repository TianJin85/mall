# -*- encoding: utf-8 -*-
"""
@File    : cart.py
@Time    :  2020/4/24 13:55
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
from datetime import datetime

from lin import db
from lin.exception import NotFound, ParameterException
from lin.interface import InfoCrud as Base
from sqlalchemy import Integer, Column, ForeignKey, and_

from app.exception.exception import Success
from app.models.comm import Commodity


class ShoppingCart(Base):
    __tablename__ = "ShoppingCart"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    userId = Column("userId", Integer, nullable=False, comment="用户id")
    commId = Column("commId", Integer, ForeignKey("Commodity.id"), nullable=False, comment="商品id")
    number = Column("number", Integer, comment="商品数量")

    @classmethod
    def append_cart(cls, form):
        cart = ShoppingCart.query.filter_by(commId=form.commId.data, userId=form.userId.data, delete_time=None).first()
        if cart:
            cart.update(
                number=form.number.data,
                commit=True
            )
        else:
            ShoppingCart.create(
                userId=form.userId.data,
                commId=form.commId.data,
                number=form.number.data,
                commit=True
            )

    @classmethod
    def remove_cart(cls, id):

        cart = ShoppingCart.query.filter_by(id=id, delete_time=None).first()
        if cart:
            cart.delete(
                commit=True
            )
        else:
            raise NotFound(msg="没有找到相关商品")

    @classmethod
    def list_cart(cls, userId):
        # cart = ShoppingCart.query.filter_by(userId=userId, delete_time=None).all()
        cart = db.session.query(ShoppingCart, Commodity).filter_by(userId=userId, delete_time=None).join(Commodity).all()
        comm_list = []
        for cart, comm in cart:
            setattr(comm, "titleImg", eval(comm["titleImg"]))   # 格式化列
            setattr(comm, "product", eval(comm["product"]))     #
            setattr(comm, "number", getattr(cart, "number"))
            comm._fields.append("number")   # 添加属性
            comm_list.append(comm)

        return comm_list

    @classmethod
    def clear_cart(cls):
        cart = ShoppingCart.query.filter_by(delete_time=None).all()
        if cart:
            date = datetime.now()
            for item in cart:
                item.update(
                    delete_time=date,
                    commit=True
                )
            return Success(msg="清空成功")
        else:
            return NotFound(msg="空空如已")