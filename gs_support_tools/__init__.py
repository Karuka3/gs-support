from flask import Flask
from flask_login import LoginManager, UserMixin
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_message = 'Need Login'
migrate = Migrate()

app = Flask(__name__)

db_uri = 'sqlite:///gs-support-tools.db'
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'karuka3'


db = SQLAlchemy(app)
db.create_all()
login_manager.init_app(app)
# db.init.app(app)
# migrate.init_app(app, db)
