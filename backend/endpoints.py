from flask import Blueprint

endpoints = Blueprint('endpoints', __name__)


# Defining routes
@endpoints.route('/')
def home():
    return "<h1>Hompage</h1>"