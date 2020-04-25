# -*- encoding: utf-8 -*-
"""
@File    : comm.py
@Time    :  2020/4/23 14:15
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
from flask import request, jsonify
from lin import admin_required
from lin.exception import Failed, ParameterException
from lin.redprint import Redprint
from werkzeug.datastructures import ImmutableMultiDict

from app.exception.exception import Success, Result, ListResult
from app.models.comm import Commodity
from app.validators.comm import CommForm, PutCommForm

comm_api = Redprint('admin')


@comm_api.route('/add_comm', methods=['POST'])
@admin_required
def add_comm():
    """
    添加商品信息
    :return:
    """
    data = eval(str(request.data, encoding='utf-8'))
    form = CommForm(ImmutableMultiDict(data))
    if form.validate():
        Commodity.insert_comm(data)     # 添加商品到数据库
        return Success(msg="添加商品成功")
    else:
        return Failed(msg=form.errors)


@comm_api.route('/del_comm', methods=["DELETE"])
@admin_required
def del_comm():
    """
    删除商品信息
    :return:
    """
    id = request.args["id"]
    if id:
        comm = Commodity.del_comm(id)
        if comm:
            return Success(msg="删除商品成功")
        else:
            return Failed(msg="此商品不存在")
    else:
        return Failed(msg="请传入商品id")


@comm_api.route('/put_comm', methods=["PUT"])
@admin_required
def put_comm():
    """
    更新商品信息
    :return:
    """
    data = eval(str(request.data, encoding='utf-8'))
    form = PutCommForm(ImmutableMultiDict(data))
    if form.validate():
        if Commodity.update_comm(data):
            return Success(msg="更新商品成功")

    else:
        return Failed(msg=form.errors)


@comm_api.route('/query_comm', methods=["GET"])
@admin_required
def query_comm():
    """商品分页查询"""
    pageNumber = request.args["pageNumber"]     # 当前获取当前页数
    if pageNumber:
        comm = Commodity.query_comm(pageNumber=int(pageNumber))
        # result = Result()
        # setattr(result, "total", Commodity.query_page_sum())

        return ListResult(total=Commodity.query_page_sum(), data=comm)
    else:
        return ParameterException(msg="请传入查询页数")


@comm_api.route('/page_sum', methods=["GET"])
@admin_required
def query_page_sum():
    """
    获取商品总的分页数
    :return: number
    """

    return Result(data=Commodity.query_page_sum())


@comm_api.route('/query_comm_details', methods=["GET"])
@admin_required
def query_comm_details():
    """
    根据商品id查询商品的详细信息
    :return:
    """
    id = request.args["id"]
    if id:
        comm = Commodity.query_comm_details(id=id)
        setattr(comm, "product", eval(getattr(comm, "product")))

        setattr(comm, "titleImg" ,eval(getattr(comm, "titleImg")))
        return Result(data=comm)
    else:
        return ParameterException(msg="请传入商品id")






