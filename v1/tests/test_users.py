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
            "username": "Kristine Camil",
            "password": "password",
            "email": "camil@new.com",
            "role": "attendant"
        }

    def teardown(self):
        self.app_context.pop()

    def test_create_user(self):
        res = self.client.post(
            "api/v1/signup",
            data=json.dumps(self.data),
            headers={"content-type": "application/json"}
        )
        self.assertEqual(res.status_code, 201)


if __name__ == "__main__":
    unittest.main()
