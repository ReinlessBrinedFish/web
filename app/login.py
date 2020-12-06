from flask.views import View
from flask import flash, redirect, render_template, url_for
from app.forms import LoginForm


class LoginView(View):
    methods = ['GET', 'POST']

    def dispatch_request(self):
        # 加载登录Form表单
        form = LoginForm()
        # 登录Form表单提交验证通过，跳转至首页
        if form.validate_on_submit():
            flash('登录请求，用户{0}，记住我{1}'.format((form.username.data, form.remember_me.data)))
            return redirect(url_for('hello'))

        return render_template('login/login.html', title='登录', form=form)
