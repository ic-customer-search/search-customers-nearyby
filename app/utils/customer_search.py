from typing import List

from exceptions import InvalidFormatException
from utils.distance_calculator import get_arc_length


def get_customer_distance(customer_dict: dict, point: List[int], radius=6371) -> int:
    if "latitude" not in customer_dict or "longitude" not in customer_dict:
        raise InvalidFormatException("Customer dict is missing latitude or longitude")

    if type(point) is not list or len(point) != 2:
        raise InvalidFormatException("Point object should be a list object of size 2")

    customer_location = [float(customer_dict["latitude"]),
                         float(customer_dict["longitude"])]
    return round(get_arc_length(radius, customer_location, point), 0)

