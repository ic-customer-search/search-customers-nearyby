import unittest

from exceptions import InvalidFormatException
from utils.distance_calculator import get_arc_length


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
