import unittest
import json

from app import create_app


class TestOrders(unittest.TestCase):
    def setUp(self):
        self.app = create_app("test")
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

        self.login_one = {
            "email": "et@new.com",
            "password": "password"
        }
        self.login_two = {
            "email": "camil@new.com",
            "password": "pass"
        }

    def teardown(self):
        self.app_context.pop()

    def test_create_user(self):
        data = {
            "username": "Kristine Camil",
            "password": "password",
            "email": "camil@new.com",
            "role": "attendant"
        }
        res = self.client.post(
            "api/v1/signup",
            data=json.dumps(data),
            headers={"content-type": "application/json"}
        )
        self.assertEqual(res.status_code, 201)

    # signin user
    def test_signin_user(self):
        login = {
            "email": "camil@new.com",
            "password": "password"
        }
        res = self.client.post(
            "api/v1/signin",
            data=json.dumps(login),
            headers={"content-type": "application/json"}
        )
        self.assertEqual(res.status_code, 404)

    # test for user who gives a wrong password
    def test_signin_user_with_wrong_pass(self):
        res = self.client.post(
            "api/v1/signin",
            data=json.dumps(self.login_two),
            headers={"content-type": "application/json"}
        )
        self.assertEqual(res.status_code, 404)

    # singin user who doesnt exist
    def test_signin_user_who_doesnt_exist(self):
        res = self.client.post(
            "api/v1/signin",
            data=json.dumps(self.login_one),
            headers={"content-type": "application/json"}
        )
        self.assertEqual(res.status_code, 404)


if __name__ == "__main__":
    unittest.main()
