# -*- encoding: utf-8 -*-
"""
@File    : cart.py
@Time    :  2020/4/25 10:06
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
from flask import request
from lin.exception import ParameterException
from werkzeug.datastructures import ImmutableMultiDict

from app.exception.exception import Success, Result
from app.models.cart import ShoppingCart

from lin.redprint import Redprint

from app.validators.cart import Append_Cart

api_cart = Redprint('cart')


@api_cart.route("/append", methods=["POST"])
def append_cart():
    data = eval(str(request.data, encoding='utf-8'))
    form = Append_Cart(ImmutableMultiDict(data))
    if form.validate():
        ShoppingCart.append_cart(form)
        return Success(msg="加入购物成功")
    else:
        return ParameterException(msg=form.errors)


@api_cart.route("/remove", methods=["DELETE"])
def remove_cart():
    id = request.args["id"]
    if id:
        ShoppingCart.remove_cart(id)
        return Success(msg="移除成功")
    else:
        return ParameterException(msg="请传入商品id")


@api_cart.route("/list", methods=["GET"])
def list_cart():
    userId = request.args["userId"]
    if userId:
        cart = ShoppingCart.list_cart(userId=userId)
        return Result(data=cart)
    else:
        return ParameterException(msg="用户id不能为空")


@api_cart.route("/clear", methods=["DELETE"])
def clear_cart():
    cart = ShoppingCart.clear_cart()

    return cart


