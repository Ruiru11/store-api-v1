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
            "name": "Jone Doe",
            "description": "['paint','wood','nails','T.cost=3000']"
        }

    def teardown(self):
        self.app_context.pop()

    def test_create_sale(self):
        res = self.client.post(
            "api/v1/sales",
            data=json.dumps(self.data),
            headers={"content-type": "application/json"}
        )
        self.assertEqual(res.status_code, 201)

    def test_get_sales(self):
        res = self.client.get(
            "api/v1/sales",
            headers={"content-type": "application/json"}
        )
        self.assertEqual(res.status_code, 200)

    def test_get_sales_by_id(self):
        res = self.client.get(
            "api/v1/sales",
            headers={"content-type": "application/json"}
        )
        self.assertEqual(res.status_code, 200)


if __name__ == "__main__":
    unittest.main()
