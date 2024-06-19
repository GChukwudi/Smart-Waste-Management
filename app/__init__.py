from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
login_manager = LoginManager()
bcrypt = Bcrypt()
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '1c19601034ac56d15b52f9a21c3f3538e016db97d3ba76da2685fa7e668d1dc0'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://adminuser:mypassword@localhost/smart_waste_management'
    # app.config.from_object('config.Config')

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    # Import blueprints and register them
    from .routes import bp as main_bp
    app.register_blueprint(main_bp)

    # Import models
    from .models import User  # Example import

    return app
