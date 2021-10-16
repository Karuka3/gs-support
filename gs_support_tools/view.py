from flask import Flask, render_template, redirect, url_for, Blueprint
from flask_login import login_required
from gs_support_tools import app
from gs_support_tools.auth import auth_api

app.register_blueprint(auth_api)


@app.route('/')
def index():
    return render_template('home.html')


@app.route("/view")
@login_required
def view():
    Name = "khasegawa"
    sr_lists = [[1, 11111111111], [2, 11111111112], [3, 11111111113]]
    return render_template("view.html", name=Name, lists=sr_lists)


@app.route('/view/<sr_id>')
@login_required
def sr_page(sr_id):
    return render_template('sr_page.html', id=sr_id)


@app.route('/template')
@login_required
def template():
    return render_template('template.html')


@app.route('/redirects')
def redirects():
    return redirect(url_for('index'))
