from flask import Flask
from flask_login import LoginManager
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from os import path

"""Module description
   * this script configures all the dependencies for the application
   * flask, flask_cors, and flask_sqlalchemy are installed in venv

   author: 7056674
   date: 04.06.2022
   version: 0.0.1
   license: free
"""


# -- Defining new Database --
db = SQLAlchemy()
DB_NAME = "database.db"

# -- Path to be enabled for CORS --
FRONTEND_DOMAIN = "http://localhost:8080"


# -- Flask Application Configuragtions --
def create_app():
    # Flask application initialization
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'makethesecretkeywhateveryouwant'
    app.config.from_object(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

    # Database initialization
    db.init_app(app)

    # Flask_Login initialization
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    from .db_models import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.get(int(user_id))

    # Enable Cross-Origin Ressource Sharing for local frontend server only
    CORS(app, resources={r"/*": {"origins": f"{FRONTEND_DOMAIN}/*"}})

    #  Referencing all routes defined in seperate files
    from .endpoints import endpoints
    from .security import security

    # Defining prefixes for routes
    app.register_blueprint(endpoints, url_prefix='/')
    app.register_blueprint(security, url_prefix='/auth')


    # Create Database if not already exists
    from . import db_models
    create_database(app)

    return app

'''

'''
def create_database(app):
    if not path.exists('backend/' + DB_NAME):
        db.create_all(app=app)
        print("Created Database!")