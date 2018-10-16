import unittest

from app import create_app


class TestOrders(unittest.TestCase):
    def setUp(self):
        self.app = create_app("test")
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def teardown(self):
        self.app_context.pop()

    def test_create_user(self):
        res = self.client.post(
            "api/v1/signup",
            headers={"content-type": "application/json"}
        )
        self.assertEqual(res.status_code, 201)

    def test_user_sigin(self):
        res = self.client.post(
            "api/v1/signin",
            headers={"content-type": "application/json"}
        )
        self.assertEqual(res.status_code, 200)


if __name__ == "__main__":
    unittest.main()
