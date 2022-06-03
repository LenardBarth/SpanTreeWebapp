from . import db
from sqlalchemy import ForeignKey
from flask_login import UserMixin

class SpannigTree(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vertices = []   # List of Objects(Dicts) like {"A": 1}
    edges = []      # List of Objects(Dicts) like {"A-B": 3}
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(128))
    first_name = db.Column(db.String(128))
    last_name = db.Column(db.String(128))
    trees = db.relationship('SpanningTree')