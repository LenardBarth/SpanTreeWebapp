from flask import Blueprint

endpoints = Blueprint('endpoints', __name__)

@endpoints.route('/')
def home():
    return "<h1>Hompage</h1>"