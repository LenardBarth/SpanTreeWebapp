from flask import Blueprint, request
from flask_login import login_required, login_user, logout_user, current_user
from . import db
from .db_models import User
from werkzeug.security import generate_password_hash, check_password_hash


"""Module description
   * this script sets up routes for all APIs concerning User authentication
   * flask, flask_login are installed in venv
   * werkzeug does not have to be nstalled seperately
   * other imports are from within directory

   author: 7056674
   date: 04.06.2022
   version: 0.0.1
   license: free
"""


security = Blueprint('security', __name__)

@security.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        response_object = {"status": "success"}
        post_data = request.get_json()
        rEmail = post_data.get('email')
        rPassword = post_data.get('password')

        # check if user wit given email exists and correct password was entered
        user = User.query.filter_by(email=rEmail).first()
        if user and check_password_hash(user.password, rPassword):
            if user.authenticated == False:
                try: 
                    user.authenticated = True
                    login_user(user, remember=True)
                    response_object['message'] = "Logged in successfully!"
                    response_object['user_id'] = user.id
                except:
                    response_object["status"] = "warning"
                    response_object['message'] = "Could not log in!"
                    user.authenticated = False
            else:
                response_object["status"] = "warning"
                response_object['message'] = "Already logged in."
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
    response_object = {"status": "info"}
    response_object['message'] = "Would have renewed token"
    return response_object

@security.route('/logout', methods=['POST'])
# @login_required
def logout():
    print("logging out")
    response_object = {"status": "info"}
    if request.method == 'POST':
        post_data = request.get_json()
        user_id = post_data.get('user_id')
        try:
            user = User.query.filter_by(id=user_id).first()
            user.authenticated = False
            logout_user()
            response_object['logged_in'] = user.authenticated
            response_object['message'] = "Logged out"
        except:
            response_object = {"status": "danger"}
            response_object['message'] = "Could not log out"
    
    return response_object