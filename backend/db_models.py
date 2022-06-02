from . import db
from flask_login import UserMixin

class SpannigTree(db.Model):
    vertices = []       # List of Objects(Dicts) like {"A": 1}
    edges = []          # List of Objects(Dicts) like {"A-B": 3}


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128, unique=True))
    password = db.Column(db.String(128))
    first_name = db.Column(db.String(128))
    last_name = db.Column(db.String(128))