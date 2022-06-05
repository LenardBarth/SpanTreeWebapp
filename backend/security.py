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

# Blueprints are used to group certain routes - mostly thematically similar - together
security = Blueprint('security', __name__)

# Route where existing users log in to session
@security.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        # init response as status success - will change if errors occur
        response_object = {"status": "success"}

        # process data from request body
        post_data = request.get_json()
        rEmail = post_data.get('email')
        rPassword = post_data.get('password')

        # check if user wit given email exists and correct password was entered
        user = User.query.filter_by(email=rEmail).first()
        if user and check_password_hash(user.password, rPassword):
            # check if this user account is not already logged in
            if user.authenticated == False:
                try: 
                    user.authenticated = True
                    login_user(user, remember=True)     # from flask_login
                    response_object['message'] = "Logged in successfully!"
                    response_object['user_id'] = user.id
                except:
                    response_object["status"] = "warning"
                    response_object['message'] = "Could not log in!"
                    user.authenticated = False
            # account logged in already
            else:
                response_object["status"] = "warning"
                response_object['message'] = "Already logged in."
        # no user with given ID was found
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

@security.route('/logout', methods=['POST'])
# @login_required
def logout():
    response_object = {"status": "info"}
    if request.method == 'POST':
        post_data = request.get_json()
        user_id = post_data.get('user_id')
        try:
            # get user that is trying to log out
            user = User.query.filter_by(id=user_id).first()
            user.authenticated = False
            logout_user()   # from flask_login
            response_object['logged_in'] = user.authenticated
            response_object['message'] = "Logged out"
        except:
            response_object = {"status": "danger"}
            response_object['message'] = "Could not log out"
    
    return response_object