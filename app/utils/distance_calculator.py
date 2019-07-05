from math import acos, radians, sin, cos
from typing import List

from exceptions import InvalidFormatException


def get_central_angle(point_1, point_2):
    """
    Calculate central angle to be used in the arc length calculator
    """
    radian_point_1 = [radians(deg) for deg in point_1]
    radian_point_2 = [radians(deg) for deg in point_2]
    delta_long = radians(point_2[1] - point_1[1])
    acos_input = sin(radian_point_1[0]) * sin(radian_point_2[0]) + cos(radian_point_1[0]) * cos(
        radian_point_2[0]) * cos(delta_long)
    angle = acos(acos_input)
    return angle


def get_arc_length(radius, point_1, point_2):
    """
    Return arc length of 2 points given the radius
    """
    if type(point_1) is not list or type(point_2) is not list or \
            len(point_1) != 2 or len(point_2) != 2:
        raise InvalidFormatException("Point list is invalid. It should be a list of size 2")
    central_angle = get_central_angle(point_1, point_2)
    return radius * central_angle


def get_customer_distance(customer_dict: dict, point: List[int], radius=6371) -> int:
    if "latitude" not in customer_dict or customer_dict["latitude"].strip() == "" \
            or "longitude" not in customer_dict \
            or customer_dict["longitude"].strip() == "":
        raise InvalidFormatException("Customer dict is missing latitude or longitude")

    if type(point) is not list or len(point) != 2:
        raise InvalidFormatException("Point object should be a list object of size 2")

    customer_location = [float(customer_dict["latitude"]),
                         float(customer_dict["longitude"])]
    return round(get_arc_length(radius, customer_location, point), 0)
