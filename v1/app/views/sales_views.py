from flask import Blueprint
from flask_restful import reqparse

# local import
from app.controllers.sales_controllers import Sales
from app.controllers.users_controllers import Users

usr = Users()


don_sale = Blueprint('sales', __name__, url_prefix="/api/v1")

sale_insatnce = Sales()


@don_sale.route("/sales", methods=["POST"])
@usr.logged_in
def create_sale():
    """
        The function helps handles all arguments required for creating,
        a sales record.
       Parameter:
                name:Name of employee creatin the sales order is of type str.            item:this is a list,
                contains all the information realting to a sale.
       Return:
            Arguments are passed to the create_sale() function,
            from sales_controller to create a sale order
     """
    parser = reqparse.RequestParser(bundle_errors=True)
    parser.add_argument("description", action="append", type=str,
                        help="must be given", location="json")
    parser.add_argument("name", type=str, required=True,
                        help="this cannot be empty", location="json")
    data = parser.parse_args()

    return sale_insatnce.create_sale(data)


@don_sale.route("/sales", methods=["GET"])
@usr.logged_in
@usr.check_admin
def get_sales(user_role=None):
    """The function is used to get all sales created"""
    return sale_insatnce.get_sales()


@don_sale.route("/sales/<int:id>", methods=["GET"])
@usr.logged_in
@usr.check_admin
def get_sale(id,user_role=None):
    """The function gets a single order using its id"""
    return sale_insatnce.get_sale(id)
