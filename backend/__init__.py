from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy


# -- Database Connection --
db = SQLAlchemy()
DB_NAME = "database.db"


# -- Flask Application Configuragtions --
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'makethesecretkeywhateveryouwant'
    app.config.from_object(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)


    # Enable Cross-Origin Ressource Sharing for local frontend server only
    CORS(app, resources={r"/*":{'origins': "http://localhost:8080", "allow_headers": "Access-Control-Allow-Origin"}})


    #  Referencing all routes defined in seperate files
    from .endpoints import endpoints
    from .security import security

    # Defining prefixes for routes
    app.register_blueprint(endpoints, url_prefix='/')
    app.register_blueprint(security, url_prefix='/auth')

    return app