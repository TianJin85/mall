# -*- encoding: utf-8 -*-
"""
@File    : cart.py
@Time    :  2020/4/26 15:47
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
from wtforms import DateTimeField, PasswordField, FieldList, IntegerField, StringField, TextField, Form, BooleanField
from wtforms.validators import DataRequired, Regexp, EqualTo, length, Optional, NumberRange


class Append_Cart(Form):
    userId = IntegerField("用户id", validators=[DataRequired(message="用户id不能为空")])
    commId = IntegerField("商品id", validators=[DataRequired(message="商品id不能为空")])
    number = IntegerField("收藏数量", validators=[DataRequired(message="收藏数量不能为空")])
