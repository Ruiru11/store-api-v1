from flask import jsonify, make_response


class Sales(object):
    """This is a class for handling all sales activities. """

    def __init__(self):
        """The constructor for sales class."""

        # creates an empty list
        self.sales = []

    def create_sale(self, data):
        """
        The function creates a new sale order.
        Parameter:
                  data:This are values that are passed,
                        they are defined and handled
                        in sales_views.py
        Returns:
                Sales:A sale record  
        """
        # generating an id
        sale_id = len(self.sales) + 1
        sale = {"id": sale_id,
                "name": data["name"], "description": data["description"]}
        # adding sale to sales list
        self.sales.append(sale)
        response_object = {
            "message": "sale record created",
            "status": "pass"
        }
        return(make_response(jsonify(response_object)), 201)

    def get_sales(self):
        """
        The function to get all sales created.
        Returns:
            products: A list of all created sales.
        """
        return(jsonify(self.sales))

    def get_sale(self, id):
        """
        The function to get a specific sale record.
        Parameter:
                id: This is the unique identification number
                 of a sale order
        Returns:
                Sales:A single sale order
        """
        for i, sale in enumerate(self.sales):
            if sale['id'] == id:
                return(make_response(jsonify(sale)))
                break
        response_object = {
            "message": "sale with that id does not exist",
            "status": "fail"
        }
        return(make_response(jsonify(response_object)), 404)
