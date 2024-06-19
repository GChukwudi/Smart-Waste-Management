# #!/usr/bin/python3

# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from flask_login import LoginManager
# from flask_wtf.csrf import CSRFProtect
# from app.config import Config

# db = None

# migrate = Migrate()
# login = LoginManager()
# login.login_view = 'auth.login'
# csrf = CSRFProtect()


# def create_app():
#     global db

#     app = Flask(__name__)
#     app.config.from_object(Config)

#     from app.routes import bp as main_bp

#     db = SQLAlchemy()
#     migrate.init_app(app, db)
#     login.init_app(app)
#     csrf.init_app(app)

#     app.register_blueprint(main_bp)

#     return app


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    login.init_app(app)

    # Import blueprints and register them
    from .routes import bp as main_bp
    app.register_blueprint(main_bp)

    # Import models
    from .models import User  # Example import

    return app
