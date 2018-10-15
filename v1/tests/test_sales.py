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

    def test_create_sale(self):
        pass

    def test_get_sales(self):
        pass

    def test_get_sales_by_id(self):
        pass


if __name__ == "__main__":
    unittest.main()
