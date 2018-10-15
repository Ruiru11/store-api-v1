import unittest


from app.v1 import create_app


class TestOrders(unittest.TestCase):
    def setUp(self):
        self.app = create_app("test")
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def teardown(self):
        self.app_context.pop()

    def test_create_product(self):
        pass

    def test_get_all_products(self):
        pass

    def test_get_product_by_id(self):
        pass


if __name__ == "__main__":
    unittest.main()
