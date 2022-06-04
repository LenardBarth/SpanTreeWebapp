from flask import Blueprint

endpoints = Blueprint('endpoints', __name__)


# Defining routes
@endpoints.route('/')
def home():
    return '<body style="background-color:#272727; width:98vw; height=100vh"><h1>Hompage</h1></body>'

@endpoints.route('/newVertex', methods=["POST"])
def newVertex():
    return '<body style="background-color:#272727; width:98vw; height=100vh"><h1>Hompage</h1></body>'

@endpoints.route('/updateVertex', methods=["UPDATE"])
def updateVertex():
    return '<body style="background-color:#272727; width:98vw; height=100vh"><h1>Hompage</h1></body>'

@endpoints.route('/newEdge', methods=["POST"])
def newEdge():
    return '<body style="background-color:#272727; width:98vw; height=100vh"><h1>Hompage</h1></body>'

@endpoints.route('/updateEdge', methods=["UPDATE"])
def updateEdge():
    return '<body style="background-color:#272727; width:98vw; height=100vh"><h1>Hompage</h1></body>'