from flask import Flask, render_template, redirect, url_for
from flask_login import login_required
from . import app
from .auth import auth_api
from .models import SR_lists
from datetime import datetime, timedelta

app.register_blueprint(auth_api)


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/view')
# @login_required
def view():
    Name = "khasegawa"
    min_date = datetime.now() - timedelta(days=7)
    sr_lists = SR_lists.query
    return render_template("sr_view.html", name=Name, min_date=min_date.date(), lists=sr_lists)


@app.route('/view/<sr_id>')
# @login_required
def sr_page(sr_id):
    return render_template('sr_page.html', id=sr_id)


@app.route('/template')
@login_required
def template():
    return render_template('template.html')


@app.route('/redirects')
def redirects():
    return redirect(url_for('index'))
