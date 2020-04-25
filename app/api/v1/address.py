# -*- encoding: utf-8 -*-
"""
@File    : address.py
@Time    :  2020/4/25 10:01
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
from flask_jwt_extended import jwt_required

from app.models.address import Address

from lin.redprint import Redprint

api_address = Redprint('address')


@api_address.route("/append", methods=["POST"])
@jwt_required
def append():

    return "添加成功"
