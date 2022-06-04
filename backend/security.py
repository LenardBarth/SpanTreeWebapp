from flask import Blueprint, request
from flask_login import login_required, login_user, logout_user, current_user
from . import db
from .db_models import User
from werkzeug.security import generate_password_hash, check_password_hash


security = Blueprint('security', __name__)

@security.route('/login', methods=['POST'])
def login():
    print("method:", request.method)
    if request.method == 'POST':
        response_object = {"status": "success"}
        post_data = request.get_json()
        rEmail = post_data.get('email')
        rPassword = post_data.get('password')

        # check if user wit given email exists and correct password was entered
        user = User.query.filter_by(email=rEmail).first()
        if user and check_password_hash(user.password, rPassword):
            user.authenticated = True
            login_user(user, remember=True)
            response_object['message'] = "Logged in successfully!"
        else:
            response_object["status"] = "warning"
            response_object['message'] = "Login data incorrect."

    return response_object

@security.route('/createUser', methods=['POST'])
def createUser():
    if request.method == 'POST':
        response_object = {"status": "success"}
        post_data = request.get_json()

        rEmail = post_data.get('email')
        rFirstName = post_data.get('first_name')
        rLastName = post_data.get('last_name')
        rPassword = post_data.get('password')

        response_object['email'] = rEmail
        response_object['first_name'] = rFirstName
        response_object['last_name'] = rLastName
        response_object['password'] = rPassword

        # check if user already exists
        user = User.query.filter_by(email=rEmail).first()
        if user:
            # If user is found means cannot create new user with this email
            response_object["status"] = "warning"
            response_object['message'] = "Email already taken!"
        else:
            try:
                newUser = User(email=rEmail, password=generate_password_hash(rPassword, method='sha256'), first_name=rFirstName, last_name=rLastName)
                db.session.add(newUser)
                db.session.commit()
                response_object['message'] = "New Account created successfully!"
            except:
                response_object["status"] = "warning"
                response_object['message'] = "Failed to create new user"
                
    return response_object

@security.route('/renew', methods=['GET'])
def renewToken():
    response_object = {"status": "success"}
    response_object = {"status": "info"}
    response_object['message'] = "Would have renewed token"
    return response_object

@security.route('/logout', methods=['GET'])
@login_required
def logout():
    response_object = {"status": "info"}
    try:
        current_user.authenticated = False
        logout_user()
        response_object['message'] = "Logged out successfully"
    except:
        response_object = {"status": "error"}
        response_object['message'] = "Could not log out"
    return response_object