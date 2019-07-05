import unittest

from customer import Customer
from exceptions import InvalidFormatException
from utils.distance_calculator import get_arc_length, get_customer_distance


class DistanceCalculatorTest(unittest.TestCase):

    def test_get_arc_length_with_invalid_input(self):
        point_1 = [52.833502, -8.522366]
        point_2 = []
        radius = 6371
        self.assertRaises(InvalidFormatException, get_arc_length, radius, point_1, point_2)

    def test_get_arc_length_with_valid_input(self):
        point_1 = [52.833502, -8.522366]
        point_2 = [53.339428, -6.257664]
        radius = 6371
        self.assertEqual(round(get_arc_length(radius, point_1, point_2), 1), 161.4)

    def test_get_customer_distance_for_valid_customer(self):
        record = {"latitude": "52.833502", "user_id": 29, "name": "Oliver Ahearn", "longitude": "-8.522366"}
        customer = Customer(record)
        center = [53.339428, -6.257664]
        distance = get_customer_distance(customer, center)
        self.assertEqual(distance, 161)

    def test_get_customer_distance_for_invalid_data(self):

        with self.assertRaises(InvalidFormatException):
            center = [53.339428, -6.257664]
            invalid_customer_data = {}
            get_customer_distance(Customer(invalid_customer_data), center)

        with self.assertRaises(InvalidFormatException):
            invalid_center = []
            valid_record = {"latitude": "52.833502", "user_id": 29, "name": "Oliver Ahearn", "longitude": "-8.522366"}
            get_customer_distance(Customer(valid_record), invalid_center)
