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

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')  # Load your configuration from a config file

    db.init_app(app)  # Initialize SQLAlchemy with the Flask app

    # Import blueprints and register them with the app
    from .routes import bp as main_bp
    app.register_blueprint(main_bp)

    # Import models (if not using application factory pattern, import here)
    from .models import User  # Example import

    return app
