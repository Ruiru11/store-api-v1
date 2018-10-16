from flask import Blueprint
from flask_restful import reqparse

# local import
from app.controllers.sales_controllers import Sales


don_sale = Blueprint('sales', __name__, url_prefix="/api/v1")

sale_insatnce = Sales()


@don_sale.route("/sales", methods=["POST"])
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
    parser = reqparse.RequestParser()
    parser.add_argument("description", action="append", type=str,
                        help="must be given", location="json")
    parser.add_argument("name", type=str, required=True,
                        help="this cannot be empty", location="json")
    data = parser.parse_args()

    return sale_insatnce.create_sale(data)
