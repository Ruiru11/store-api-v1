from flask import Blueprint
from flask_restful import reqparse


don_user = Blueprint('users', __name__, url_prefix='api/v1')


@don_user.route('/signin', methods=["POST"])
def signin():
    parser = reqparse.RequestParser()
    parser.add_argument("email", type=str, required=True,
                        help="name required", location="json")
    parser.add_argument("password", type=str, required=True,
                        help="name required", location="json")
    data = parser.parse_args()
    return True


@don_user.route("/signup", methods=["POST"])
def signup():
    parser = reqparse.RequestParser()
    parser.add_argument("email", type=str, required=True,
                        help="email required", location="json")
    parser.add_argument("name", type=str, required=True,
                        help="name required", location="json")
    parser.add_argument("password", type=str, required=True,
                        help="password required", location="json")
    data = parser.parse_args()
    return True
