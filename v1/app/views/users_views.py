from flask import Blueprint
from flask_restful import reqparse

# local imports
from app.controllers.users_controllers import Users

don_user = Blueprint('users', __name__, url_prefix="/api/v1")

user_instance = Users()


@don_user.route("/signup", methods=["POST"])
def create_user():
    """
    This function creates a new user. 

    Parameters:
            username:Name to be used by user once account is created.
            email:Email to be used for verification.
            Password: To be used when signin to created account. 
                        role: This is the role of user can be attendant/admin
    Returns:
            Users:Creates a new user. 


    """
    parser = reqparse.RequestParser()
    parser.add_argument("username", type=str, required=True,
                        help="field cannot be empty", location="json")
    parser.add_argument("email", type=str, required=True,
                        help="field cannot be empty", location="json")
    parser.add_argument("password", type=str, required=True,
                        help="field cannot be empty", location="json")
    parser.add_argument("role", type=str, required=True,
                        help="fiels cannot be empty", location="json")
    data = parser.parse_args()

    return user_instance.create_user(data)
