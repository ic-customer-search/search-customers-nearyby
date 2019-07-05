import unittest

from config import SEARCH_CENTER_LAT, SEARCH_CENTER_LONG
from utils.distance_calculator import get_arc_length


class DistanceCalculatorTest(unittest.TestCase):

    def test_arc_length(self):
        point_1 = [52.833502, -8.522366]
        point_2 = [SEARCH_CENTER_LAT, SEARCH_CENTER_LONG]

        self.assertEqual(get_arc_length(point_1, point_2), 161.4)