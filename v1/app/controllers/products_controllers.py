from flask import jsonify, make_response


class Products(object):
    """This is a class for handling all product activities."""

    def __init__(self):
        """The constructor for products class. """
        # creates an empty list
        self.items = []

    def create_item(self, data):
        """
        The function to create a new product.

        Parameter:
            data:This are the values to be passed,
                 they are defined in product_views.py

        Returns:
            Products: A product with all data passed and a
                        unique id
        """
        # generating an id
        item_id = len(self.items) + 1
        item = {"id": item_id, "name": data['name'],
                "price": data['price'],
                "description": data['description'],
                "category": data['category']}
        self.items.append(item)
        response_object = {
            "status": "success",
            "message": "order created successfully"
        }
        return(make_response(jsonify(response_object)), 201)

    def get_items(self):
        """
        The function to get all products created.

        Returns:
            products: A list of all created products.
        """
        return(jsonify(self.items))

    def get_item(self, id):
        """
        The function to get a specific product usiing its unique id.return.

        Parameters:
            id: This is the identiication number of product to be viewed.

        Returns:
            Products: A single product


        """
        for i, item in enumerate(self.items):
            print(item['id'], id)
            if item['id'] == id:
                print(item)
                return(make_response(jsonify(item)))
                break
        response_object = {
            "message": "no item with that id",
            "status": "fail"
        }
        return(make_response(jsonify(response_object)), 404)
