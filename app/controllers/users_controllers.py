from flask import jsonify, make_response, request
import jwt
import datetime
from functools import wraps
import re


class Users(object):
    """This function deals with all user activities"""

    def __init__(self):
        """The constructor for users class"""

        # create empty list
        self.users = []

    def validate_email(self, email):
        """The function validates the email"""
        match = re.match(
            r'(^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$)',
            email)
        if match is None:
            response_object = {
                "status": "fail",
                "message": "Please enter a valid email"
            }
            return(make_response(jsonify(response_object)), 422)
        elif len(email) == '':
            response_object = {
                "status": "fail",
                "message": " email cannot be empty"
            }
            return(make_response(jsonify(response_object)),422)
        else:
            return True

    def validate_password(self, password):
        """The function validates the password"""
        match = re.match(r'[a-z]{4,}', password)
        if match is None:

            response_object = {
                "status": "fail",
                "message": "password format wrong"
            }
            return(make_response(jsonify(response_object)),422)
        elif len(password) == 0:
            response_object = {
                "status": "fail",
                "message": " password cannot be empty"
            }
            return(make_response(jsonify(response_object)), 422)
        else:
            return True

    def validate_username(self, username):
        """The function validates the username"""
        if len(username) < 4:
            response_object = {
                "status": "fail",
                "message": "username to short"
            }
            return(make_response(jsonify(response_object)))
        elif len(username) > 7:
            response_object = {
                "status": "fail",
                "message": "username too long"
            }
            return(make_response(jsonify(response_object)))
        else:
            return True

    def create_user(self, data):
        """
        The function to create new users. 

        Parameters:
                data:This are the arguments passed,
                                they are defined in user_views file.


        Returns:
                Users:A new user with a uniqu id. 

        """
        username = self.validate_username(data['username'])
        email = self.validate_email(data['email'])
        password = self.validate_password(data['password'])
        if password and username and email is True:
            user_id = len(self.users) + 1
            user = {"id": user_id, "username": data["username"],
                    "email": data["email"],
                    "password": data["password"], "role": data["role"]}
            self.users.append(user)
            response_object = {
                "message": "User created successfully",
                "status": "pass"
            }
            return(make_response(jsonify(response_object)), 201)
        elif password is not True:
            return password
        elif email is not True:
            return email
        elif username is not True:
            return username
        else:
            return email and password and username

    def signin_user(self, data):
        """
        The function logs in a user.

        Parameters:
            data[email]:email used during signup.
            data[password]:password used during signup

        Returns:
            Users:Signs in a user and also generates a token.
        """
        print('users', self.users)
        for user in self.users:
            if data["email"] in dict.values(user):
                if data["password"] == user["password"]:
                    token = self.generate_token(
                        user["id"], user["username"], user["role"])
                    response_object = {
                        "message": "logged in successfully",
                        "status": "pass",
                        "token": token
                    }
                    return(make_response(jsonify(response_object)))
                else:
                    response_object = {
                        "message": "Wrong password please re-enter password",
                        "status": "fail"
                    }
                    return(make_response(jsonify(response_object)), 409)
            else:
                if data["email"] not in dict.values(user):
                    response_object = {
                        "message": "user not found please register or contact admin",
                        "status": "fail"
                    }
                    return(make_response(jsonify(response_object)), 404)

    def generate_token(self, id, username, role):
        """Generate authentication token for signin."""
        payload = {
            'exp': datetime.datetime.now() + datetime.timedelta(seconds=9000),
            'iat': datetime.datetime.now(),
            'sub': id,
            'username': username,
            'role': role
        }
        return jwt.encode(
            payload,
            'newtothis',
            algorithm='HS256'
        ).decode("utf-8")

    def logged_in(self, func):
        @wraps(func)
        def decorator(*args, **kwargs):
            try:
                token = request.headers.get('Authorization')
                payload = jwt.decode(token, 'newtothis')
                user_id = payload['sub']
                for user in self.users:
                    if user_id in dict.values(payload):
                        responseObject = {
                            'staus': 'sucess',
                            'message': 'user logged in'
                        }
                        new_kwargs = {
                            'res': responseObject,
                            'user_id': user[0]
                        }
                        kwargs.update(new_kwargs)
                    else:
                        responseObject = {
                            'status': 'fail',
                            'message': 'User not found'
                        }
                    return make_response(jsonify(responseObject))
            except jwt.ExpiredSignatureError:
                responseObject = {
                    'status': 'Fail',
                    'message': 'Token expired please login'
                }
                return make_response(jsonify(responseObject), 401)
            except jwt.exceptions.DecodeError:
                responseObject = {
                    'status': 'Fail',
                    'message': 'No token passed or invalid token type'
                }
                return make_response(jsonify(responseObject), 500)
            return func(*args, **kwargs)
        return decorator

    def check_admin(self, func):
        @wraps(func)
        def decorator(*args, **kwargs):
            try:
                token = request.headers.get('Authorization')
                payload = jwt.decode(token, 'newtothis')
                user_role = payload['role']
                if user_role == 'admin':
                    new_kwargs = {
                        'user_role': user_role
                    }
                    kwargs.update(new_kwargs)
                else:
                    responseObject = {
                        'status': 'fail',
                        'message': 'Un-authorized only admin allowed'
                    }
                    return make_response(jsonify(responseObject), 401)
            except jwt.ExpiredSignatureError:
                responseObject = {
                    'status': 'Fail',
                    'message': 'Token expired please login'
                }
                return make_response(jsonify(responseObject), 401)
            return func(*args, **kwargs)
        return decorator
