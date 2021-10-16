from flask import Flask, render_template, url_for, redirect, request, Blueprint, session, flash, abort
from flask_login import login_user, logout_user, login_required, LoginManager, UserMixin, current_user
from . import login_manager, bcrypt, db
from .forms import RegistrationForm, LoginForm
from .models import User


auth_api = Blueprint('auth', __name__, url_prefix="/auth",
                     template_folder='templates')


@login_manager.user_loader
def user_loader(user_id):
    return User.query.get(int(user_id))


@login_manager.request_loader
def request_loader(request):
    pass


@auth_api.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not bcrypt.check_password_hash(user.password, form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, form.remember.data)
        flash('You have been logged in!', 'success')
        return redirect(request.args.get("next") or url_for('index'))
    return render_template('login.html', form=form)


@ auth_api.route('/logout')
@ login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@ auth_api.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')
        user = User(username=form.username.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', 'Success')
        return redirect(url_for('auth.login'))
    return render_template('register.html', form=form)
