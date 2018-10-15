from flask import Blueprint
from flask_restful import reqparse

don_item = Blueprint('products', __name__, url_prefix="api/v1")


@don_item.route("/products", methods=["POST"])
def create_item():
    parser = reqparse.RequestParser()
    parser.add_argument("name", type=str, required=True,
                        help="name required", location="json")
    parser.add_argument("category", type=str, required=True,
                        help="name required", location="json")
    parser.add_argument("price", type=str, required=True,
                        help="name required", location="json")
    data = parser.parse_args()
    return True


@don_item.route("/products", methods=["GET"])
def get_items():
    return True


@don_item.route("/products<int:id", methods=["GET"])
def get_item():
    return True
