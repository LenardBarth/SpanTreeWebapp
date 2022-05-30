from flask import Blueprint

security = Blueprint('security', __name__)

@security.route('/login', methods=['POST'])
def login():
    return "<p>Login</p>"

@security.route('/createUser', methods=['POST'])
def signUp():
    return "<p>sign up</p>"

@security.route('/renew', methods=['GET'])
def renewToken():
    return "<p>renew token</p>"

@security.route('/logout', methods=['POST'])
def logout():
    return "<p>logout</p>"