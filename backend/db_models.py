from email.policy import default
from . import db
from datetime import datetime
from sqlalchemy import ForeignKey, func
from flask_login import UserMixin

# database class (table) to store and load projects of spanning trees
class SpanningTree(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    vertices = db.Column(db.Text)
    edges =  db.Column(db.Text)
    result =  db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))   # used to represent ONE to MANY relation (one user can have many trees; one tree can only belong to one user)

# database class (table) to store user accounts
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(128))
    first_name = db.Column(db.String(128))
    last_name = db.Column(db.String(128))
    authenticated = db.Column(db.Boolean, default=False)

    # Needed to confirm to login_user() function provided by flask_login
    def is_active(self):
        # True, as all users are active
        return True

    def get_id(self):
        # Return users ID as string to satisfy Flask-Login's requirements
        return str(self.id)

    def is_authenticated(self):
        # Return True if the user is authenticated
        return self.authenticated

    def is_anonymous(self):
        # False, as anonymous users aren't supported
        return False