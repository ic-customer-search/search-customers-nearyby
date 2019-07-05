import unittest

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
        customer_dict = {"latitude": "52.833502", "user_id": 29, "name": "Oliver Ahearn", "longitude": "-8.522366"}
        center = [53.339428, -6.257664]
        distance = get_customer_distance(customer_dict, center)
        self.assertEqual(distance, 161)

    def test_get_customer_distance_for_invalid_customer(self):
        center = [53.339428, -6.257664]

        with self.assertRaises(InvalidFormatException):
            invalid_customer_dict = {}
            get_customer_distance(invalid_customer_dict, center)

        with self.assertRaises(InvalidFormatException):
            invalid_customer_dict = {"latitude": "53.22"}
            get_customer_distance(invalid_customer_dict, center)

        with self.assertRaises(InvalidFormatException):
            invalid_customer_dict = {"latitude": "", "longitude": ""}
            get_customer_distance(invalid_customer_dict, center)

        with self.assertRaises(InvalidFormatException):
            invalid_customer_dict = {"longitude": "50"}
            get_customer_distance(invalid_customer_dict, center)

        with self.assertRaises(InvalidFormatException):
            valid_customer_dict = {"latitude": "52.833502", "user_id": 29, "name": "Oliver Ahearn", "longitude": "-8.522366"}
            get_customer_distance(valid_customer_dict, [])


