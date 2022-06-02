from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'makethesecretkeywhateveryouwant'
    app.config.from_object(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    CORS(app, resources={r"/*":{'origins': "http://localhost:8080", "allow_headers": "Access-Control-Allow-Origin"}})

    from .endpoints import endpoints
    from .security import security

    app.register_blueprint(endpoints, url_prefix='/')
    app.register_blueprint(security, url_prefix='/auth/api/v1')

    return app