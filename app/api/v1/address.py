# -*- encoding: utf-8 -*-
"""
@File    : address.py
@Time    :  2020/4/25 10:01
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
from flask import request
from flask_jwt_extended import jwt_required
from lin.exception import ParameterException
from werkzeug.datastructures import ImmutableMultiDict

from app.exception.exception import Success, Result
from app.models.address import Address

from lin.redprint import Redprint

from app.validators.address import AddressAppend, AddressAmend

api_address = Redprint('address')


@api_address.route("/append", methods=["POST"])
# @jwt_required
def append():
    data = eval(str(request.data, encoding='utf-8'))
    form = AddressAppend(ImmutableMultiDict(data))

    if form.validate():
        Address.append(data)
        return Success(msg="添加地址成功")
    else:
        return ParameterException(msg=form.errors)


@api_address.route("/amend", methods=["PUT"])
def amend():
    data = eval(str(request.data, encoding='utf-8'))
    form = AddressAmend(ImmutableMultiDict(data))

    if form.validate():
        Address.amend_default_address(form)
        return Success(msg="更改地址成功")
    else:
        return ParameterException(msg=form.errors)


@api_address.route("/list", methods=["GET"])
def address_list():
    userId = request.args["userId"]
    if userId:
        address = Address.address_list(userId=userId)
        return Result(data=address)
    else:
        return ParameterException(msg="请传入用户id")


@api_address.route("/delete", methods=["GET"])
def address_delete():
    id = request.args["id"]
    if id:
        Address.delete_address(id=id)
        return Success(msg="删除成功")
    else:
        return ParameterException(msg="请传入地址id")



