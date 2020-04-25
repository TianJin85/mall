# -*- encoding: utf-8 -*-
"""
@File    : user.py
@Time    :  2020/4/24 14:10
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
from flask import request
from lin import db
from lin.exception import Success, Failed
from lin.jwt import identity
from lin.redprint import Redprint
from werkzeug.datastructures import ImmutableMultiDict
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity,
    create_refresh_token)


from app.models.user import UserInfo
from app.validators.user import Register, Login

api_user = Redprint("user")


@api_user.route("/register", methods=["POST"])
def register():
    data = eval(str(request.data, encoding='utf-8'))
    form = Register(ImmutableMultiDict(data))
    if form.validate():     # 数据校验
        UserInfo.register_user(form)

        return Success(msg="注册成功")
    else:
        return form.errors


@api_user.route("/login", methods=['POST'])
def login():

    data = eval(str(request.data, encoding='utf-8'))
    form = Login(ImmutableMultiDict(data))

    if form.validate():     # 数据校验
        user = db.session.query(UserInfo).filter(UserInfo.nickName == form.nickName.data).first()
        if user and user.check_password(form.passWord.data):
            identity['uid'] = user.id
            access_token = create_access_token(identity=identity)
            refresh_token = create_refresh_token(identity=identity)
            return {"access_token": access_token, "refresh_token": refresh_token}
        else:
            return Failed(msg="获取token失败")
    else:
        return Failed(msg=form.errors)


@api_user.route("/amend", methods=["PUT"])
@jwt_required
def amend():
    return "授权成功"
    #
    # data = eval(str(request.data, encoding='utf-8'))
    # form = Login(ImmutableMultiDict(data))
    #
    # if form.validate():  # 数据校验
    #     user = db.session.query(UserInfo).filter(UserInfo.nickName == form.nickName.data).first()
    #     if user and user.check_password(form.passWord.data):
    #
    #         return Success(msg="修改密码成功")

