from email.policy import default
from . import db
from datetime import datetime
from sqlalchemy import ForeignKey, func
from flask_login import UserMixin

class SpanningTree(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vertices = []   # List of Objects(Dicts) like {"A": 1}
    edges = []      # List of Objects(Dicts) like {"A-B": 3}
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    last_modified = db.Column(db.DateTime(timezone=True), onupdate=func.now())


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(128))
    first_name = db.Column(db.String(128))
    last_name = db.Column(db.String(128))
    authenticated = db.Column(db.Boolean, default=False)
    trees = db.relationship('SpanningTree')

    # Needed to confirm to login_user() function provided by flask_login
    def is_active(self):
        # True, as all users are active
        return True

    def get_id(self):
        # Return the email address to satisfy Flask-Login's requirements
        return self.id

    def is_authenticated(self):
        # Return True if the user is authenticated
        return self.authenticated

    def is_anonymous(self):
        # False, as anonymous users aren't supported
        return False