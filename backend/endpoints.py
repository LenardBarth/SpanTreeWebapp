from flask import Blueprint

endpoints = Blueprint('endpoints', __name__)


# Defining routes
@endpoints.route('/')
def home():
    return '<body style="background-color:#272727; width:98vw; height=100vh"><h1>Hompage</h1></body>'