# -*- encoding: utf-8 -*-
"""
@File    : comm.py
@Time    :  2020/4/23 16:54
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
from lin import manager
from wtforms import DateTimeField, PasswordField, FieldList, IntegerField, StringField, TextField, Form
from wtforms.validators import DataRequired, Regexp, EqualTo, length, Optional, NumberRange
import time

# from lin.forms import Form


class CommForm(Form):
    name = StringField("商品名称", validators=[DataRequired(message="商品名称不能为空"),
                                           length(min=2, max=500, message='商品名长度必须在2~250之间')])
    pepertory = IntegerField("商品库存", validators=[DataRequired(message="商品库存不能为空")])
    titleImg = StringField("商品标题图片", validators=[DataRequired(message="商品标题图片不能为空"),
                                                 length(min=2, max=250, message='商品名长度必须在2~250之间')])
    detailsImg = StringField("商品详情", validators=[DataRequired(message="商品详情不能为空")])
    type = StringField("产品类型", validators=[DataRequired(message="产品类型不能为空")])
    product = StringField("产品型号", validators=[DataRequired(message="产品型号不能为空")])


class PutCommForm(CommForm):
    id = IntegerField("商品id", validators=[DataRequired(message="商品id不能为空")])