import unittest


class CustomerSearchTest(unittest.TestCase):

    def test_get_customer_distance(self):
        customer = {"latitude": "53.74452", "user_id": 29, "name": "Oliver Ahearn", "longitude": "-7.11167"}