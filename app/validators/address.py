# -*- encoding: utf-8 -*-
"""
@File    : address.py
@Time    :  2020/4/26 11:17
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
from wtforms import DateTimeField, PasswordField, FieldList, IntegerField, StringField, TextField, Form, BooleanField
from wtforms.validators import DataRequired, Regexp, EqualTo, length, Optional, NumberRange


class AddressAppend(Form):
    """
    添加地址数据校验
    """
    userId = IntegerField("用户id", validators=[DataRequired(message="用户id不能为空")])
    userName = StringField("用户名称", validators=[DataRequired(message="用户名称不能为空")])
    address = StringField("用户地址", validators=[DataRequired(message="用户地址不能为空")])
    phoneCode = StringField("电话号码", validators=[DataRequired(message="电话号码不能为空"),
                                                Regexp(r'^1[35678]\d{9}', message="电话号码必须是11位0-9组成的有效数字")])
    # default = BooleanField("默认地址", validators=[DataRequired(message="是否为默认地址不能为空")])


class AddressAmend(AddressAppend):
    """
    修改地址
    """
    id = IntegerField("地址id", validators=[DataRequired(message="地址id不能为空")])
