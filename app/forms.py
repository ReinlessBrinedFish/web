from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


# 自定义表单类
class LoginForm(FlaskForm):
    # StringField: 文本字段
    # PasswordField: 密码字段
    # DataRequired: 数据不可为空的验证器
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)
    # 提交按钮
    submit = SubmitField('登录')
