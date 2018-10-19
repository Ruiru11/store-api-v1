import unittest
import json


from app import create_app


class TestOrders(unittest.TestCase):
    def setUp(self):
        self.app = create_app("test")
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.data = {
            "name": "steel",
            "id": 1,
            "price": "sh.825",
            "category": "construction",
            "description": "Y16-For Columns and Slab"
        }
        self.admin = {
            "username": "prod",
            "email": "prod@gmail.com",
            "role": "admin",
            "password": "new"
        }
        self.admin_log = {
            "email": "prod@gmail.com",
            "password": "new"
        }
        self.attendant = {
            "username": "theo",
            "email": "theo@gmail.com",
            "role": "attendant",
            "password": "pass"
        }
        self.attendant_log = {
            "email": "theo@gmail.com",
            "password": "pass"
        }

    def teardown(self):
        self.app_context.pop()

    # create a user admin
    def test_create_admin_user(self):
        res = self.client.post(
            "api/v1/signup",
            data=json.dumps(self.admin),
            headers={"content-type": "application/json"}

        )
        self.assertEqual(res.status_code, 201)

    # signin in the admin to get the token
    def get_user_token(self):
        res = self.client.post(
            "api/v1/signin",
            data=json.dumps(self.admin_log),
            headers={"content-type": "application/json"}
        )
        response = json.loads(res.data.decode('utf-8'))['token']
        print("token>>>>>>>>>>>>>>>>>>>>>", response)
        return response

    # creating a product needs admin access
    def test_create_product(self):
        token = self.get_user_token()
        res = self.client.post(
            "api/v1/products",
            data=json.dumps(self.data),
            headers={"content-type": "application/json",
                     "Authorization": token
                     }
        )
        self.assertEqual(res.status_code, 201)

    # Trying to create product without a token
    def test_create_product3(self):
        res = self.client.post(
            "api/v1/products",
            data=json.dumps(self.data),
            headers={"content-type": "application/json"
                     }
        )
        self.assertEqual(res.status_code, 500)

    # getting all products can be done by both admin and attendant
    def test_get_all_products(self):
        token = self.get_user_token()
        res = self.client.get(
            "api/v1/products",
            headers={"content-type": "application/json",
                     "Authorization": token
                     }
        )
        self.assertEqual(res.status_code, 200)

    # test to get single product both admin and attendant have the right
    def test_get_product_by_id(self):
        token = self.get_user_token()
        res = self.client.get(
            "api/v1/products/1",
            headers={"content-type": "application/json",
                     "Authorization": token
                     }
        )
        self.assertEqual(res.status_code, 200)

    # getting a product that doesnot exist.
    def test_get_product_by_id1(self):
        token = self.get_user_token()
        res = self.client.get(
            "api/v1/products/2",
            headers={"content-type": "application/json",
                     "Authorization": token
                     }
        )
        self.assertEqual(res.status_code, 404)

    # create a user attendant
    def test_create_attendant_user(self):
        res = self.client.post(
            "api/v1/signup",
            data=json.dumps(self.attendant),
            headers={"content-type": "application/json"}
        )
        self.assertEqual(res.status_code, 201)


if __name__ == "__main__":
    unittest.main()
