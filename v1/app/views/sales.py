from flask import Blueprint
from flask_restful import reqparse


don_sales = Blueprint("sales", __name__, url_prefix="api/v1")


@don_sales.route("/sales", methods=["POST"])
def create_sales():
    parser = reqparse.RequestParser()
    parser.add_argument("userid",type=str)
    data = parser.parse_args()
    return True


@don_sales.route("/sales", methods=["GET"])
def get_sale():
    return True
