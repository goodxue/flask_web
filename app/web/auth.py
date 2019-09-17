from flask import render_template, flash, redirect, url_for, Blueprint
from flask_login import login_user, logout_user, login_required, current_user

from app.forms import LoginForm
from app.models import Admin
from app.helper import redirect_back

from . import auth_bp

@auth_bp.route('/login',methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('web.index'))
    
    form = LoginForm()
    if form.validate_on_submit():
        #validate_on_submit:调用is_submitted和validate方法，返回一个布尔值，用来判断表单是否被提交；
        username = form.username.data
        password = form.password.data
        remember = form.remember.data
        admin = Admin.query.first()
        if admin:
            if username == admin.username and admin.validate_password(password):
                login_user(admin, remember)
                flash('Hello sir, wellcome back!','info')
                return redirect_back()
            flash('Invalid username or password.','warning')
        else:
            flash('No account.','warning')
    return render_template('auth/login.html',form=form)

@auth_bp.route('logout')
@login_required
def logout():
    logout_user()
    flash('Goodbye sir ...','info')
    return redirect_back()