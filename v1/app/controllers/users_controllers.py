from flask import jsonify, make_response


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
        user = {"id": user_id, "username": data["username"], "email": data["email"],
                "password": data["password"], "role": data["role"]}
        self.users.append(user)
        response_object = {
            "message": "User created successfully",
            "status": "pass"
        }
        return(make_response(jsonify(response_object)), 201)
