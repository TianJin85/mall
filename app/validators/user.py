# -*- encoding: utf-8 -*-
"""
@File    : user.py
@Time    :  2020/4/24 14:19
@Author  : Tianjin
@Email   : tianjincn@163.com
@Software: PyCharm
"""
from wtforms import Form, StringField, IntegerField
from wtforms.validators import DataRequired, length, Regexp


class Login(Form):
    """
    登录数据校验
    """
    nickName = StringField("昵称", validators=[DataRequired(message="昵称不能为空"),
                                             length(min=2, max=32, message='用户名长度必须在2~10之间')])
    passWord = StringField("密码", validators=[DataRequired(message="密码不能为空"),
                                             length(min=6, max=18, message='密码长度必须在6~18之间')])


class Register(Login):
    """
    注册数据校验
    """
    phoneCode = StringField("电话号码", validators=[DataRequired(message="电话号码不能为空"),
                                                Regexp(r'^1[35678]\d{9}', message="电话号码必须是11位0-9组成的有效数字")])