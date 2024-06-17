from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from app.config import Config

db = None

migrate = Migrate()
login = LoginManager()
login.login_view = 'auth.login'
csrf = CSRFProtect()


def create_app():
    global db

    app = Flask(__name__)
    app.config.from_object(Config)

    from app.routes import bp as main_bp

    db = SQLAlchemy()
    migrate.init_app(app, db)
    login.init_app(app)
    csrf.init_app(app)

    app.register_blueprint(main_bp)

    return app
