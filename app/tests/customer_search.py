import unittest

from exceptions import InvalidFormatException
from utils.customer_search import get_customer_distance


class CustomerSearchTest(unittest.TestCase):

    def test_get_customer_distance_for_valid_customer(self):
        customer_dict = {"latitude": "52.833502", "user_id": 29, "name": "Oliver Ahearn", "longitude": "-8.522366"}
        center = [53.339428, -6.257664]
        distance = get_customer_distance(customer_dict, center)
        self.assertEqual(distance, 161)

    def test_get_customer_distance_for_invalid_customer(self):
        valid_customer_dict = {"latitude": "52.833502", "user_id": 29, "name": "Oliver Ahearn", "longitude": "-8.522366"}
        invalid_customer_dict = {}
        center = [53.339428, -6.257664]

        self.assertRaises(InvalidFormatException, get_customer_distance, invalid_customer_dict, center)
        self.assertRaises(InvalidFormatException, get_customer_distance, valid_customer_dict, [10])


