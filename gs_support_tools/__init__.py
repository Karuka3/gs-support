from flask import Flask
from flask_login import LoginManager, UserMixin
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from config import Config


login_manager = LoginManager()
login_manager.login_view = 'auth.login'
migrate = Migrate()

app = Flask(__name__)
app.config.from_object(Config)
bcrypt = Bcrypt(app)

db = SQLAlchemy(app)
db.create_all()
login_manager.init_app(app)
# db.init.app(app)
# migrate.init_app(app, db)
