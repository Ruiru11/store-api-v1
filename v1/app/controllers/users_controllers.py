from flask import jsonify, make_response
import jwt
import datetime


class Users(object):
    """This function deals with all user activities"""

    def __init__(self):
        """The constructor for users class"""

        # create empty list
        self.users = []

    def create_user(self, data):
        """
        The function to create new users. 

        Parameters:
                data:This are the arguments passed,
                                they are defined in user_views file.


        Returns:
                Users:A new user with a uniqu id. 

        """

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
                        "message": "could not login",
                        "status": "fail"
                    }
                    return(make_response(jsonify(response_object)),409)

    def generate_token(self, id, username, role):
        """Generate authentication token."""
        payload = {
            'exp': datetime.datetime.now() + datetime.timedelta(seconds=9000),
            'iat': datetime.datetime.now(),
            'sub': id,
            'username': username,
            'role': role
        }
        return jwt.encode(
            payload,
            'qwertyuiop',
            algorithm='HS256'
        ).decode("utf-8")
