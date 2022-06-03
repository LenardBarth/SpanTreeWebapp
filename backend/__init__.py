from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from os import path

# -- Defining new Database --
db = SQLAlchemy()
DB_NAME = "database.db"

# -- Path to be enabled for CORS --
FRONTEND_DOMAIN = "http://localhost:8080"


# -- Flask Application Configuragtions --
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'makethesecretkeywhateveryouwant'
    app.config.from_object(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)


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