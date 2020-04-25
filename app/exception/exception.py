# -*- encoding: utf-8 -*-
"""
@File    : exception.py
@Time    :  2020/4/25 8:59
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
from flask import json, request
from werkzeug.exceptions import HTTPException
from werkzeug._compat import text_type

from lin.exception import Success


class APIException(HTTPException):
    code = 500
    msg = '抱歉，服务器未知错误'
    error_code = 999
    data = ""

    def __init__(self, msg=None, code=None, error_code=None,
                 headers=None, data=None):
        if code:
            self.code = code
        if error_code:
            self.error_code = error_code
        if msg:
            self.msg = msg
        if data:
            self.data = data
        if headers is not None:
            headers_merged = headers.copy()
            headers_merged.update(self.headers)
            self.headers = headers_merged

        super(APIException, self).__init__(msg, None)

    def get_body(self, environ=None):
        body = dict(
            msg=self.msg,
            error_code=self.error_code,
            request=request.method + '  ' + self.get_url_no_param(),
            data=self.data
        )
        text = json.dumps(body)
        return text_type(text)

    @staticmethod
    def get_url_no_param():
        full_path = str(request.full_path)
        main_path = full_path.split('?')
        return main_path[0]

    def get_headers(self, environ=None):
        return [('Content-Type', 'application/json')]


class ListException(APIException):
    total = ""
    code = 500
    msg = '抱歉，服务器未知错误'
    error_code = 999
    data = ""

    def __init__(self, msg=None, code=None, error_code=None,
                 headers=None, data=None, total=None):
        if code:
            self.code = code
        if error_code:
            self.error_code = error_code
        if msg:
            self.msg = msg
        if data:
            self.data = data

        if total:
            self.total = total
        if headers is not None:
            headers_merged = headers.copy()
            headers_merged.update(self.headers)
            self.headers = headers_merged

        super(APIException, self).__init__(msg, None)

    def get_body(self, environ=None):
        body = dict(
            msg=self.msg,
            error_code=self.error_code,
            request=request.method + '  ' + self.get_url_no_param(),
            data=self.data,
            total=self.total
        )
        text = json.dumps(body)
        return text_type(text)

    @staticmethod
    def get_url_no_param():
        full_path = str(request.full_path)
        main_path = full_path.split('?')
        return main_path[0]

    def get_headers(self, environ=None):
        return [('Content-Type', 'application/json')]


class Result(APIException):
    code = 201
    data = ""
    msg = "查询成功"
    error_code = 200


class Success(Success):
    code = 201
    msg = '成功'
    error_code = 200


class ListResult(ListException):
    total = ""
    code = 201
    data = ""
    msg = "查询成功"
    error_code = 200


