from flask import render_template, url_for, redirect, request, Blueprint, session, abort
from flask_login import login_user, logout_user, login_required, LoginManager, current_user
from . import login_manager, bcrypt, db
from .forms import RegistrationForm, LoginForm
from .models import Template

template_api = Blueprint('template', __name__, url_prefix="/template",
                         template_folder='templates')


@template_api.route('/list')
def list():
    templates = Template.query.all()
    return render_template("template.html", templates=templates)


@template_api.route('/add', methods=["POST"])
def add():
    template = Template()
    template.text = request.form["add_text"]
    template.user_id = 0
    db.session.add(template)
    db.session.commit()
    return redirect(url_for('template.list'))


@template_api.route('/edit', methods=["POST"])
def edit():
    id = request.form["id"]
    text = request.form["text"]
    template = Template.query.filter_by(id=id).first()
    template.text = text
    db.session.commit()
    return redirect(url_for('template.list'))


@template_api.route('/delete', methods=["POST"])
def delete():
    id = request.form["id"]
    template = Template.query.filter_by(id=id).first()
    db.session.delete(template)
    db.session.commit()
    return redirect(url_for('template.list'))
