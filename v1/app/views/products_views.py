from flask import Blueprint
from flask_restful import reqparse

from app.controllers.products_controllers import Products

don_item = Blueprint('products', __name__, url_prefix="/api/v1")

product_instance = Products()


@don_item.route("/products", methods=["POST"])
def create_item():
    parser = reqparse.RequestParser()
    parser.add_argument("name", type=str, required=True,
                        help="name required", location="json")
    parser.add_argument("category", type=str, required=True,
                        help="name required", location="json")
    parser.add_argument("price", type=str, required=True,
                        help="name required", location="json")
    parser.add_argument("description", type=str, required=True,
                        help="description required", location="json")
    data = parser.parse_args()
    return product_instance.create_item(data)


@don_item.route("/products", methods=["GET"])
def get_items():
    return product_instance.get_items()


@don_item.route("/products/<int:id>", methods=["GET"])
def get_item(id):
    return product_instance.get_item(id)