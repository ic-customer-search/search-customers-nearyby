from math import acos, radians, sin, cos

from exceptions import InvalidFormatException


def get_central_angle(point_1, point_2):
    """
    Calculate central angle to be used in the arc length calculator
    """
    radian_point_1 = [radians(deg) for deg in point_1]
    radian_point_2 = [radians(deg) for deg in point_2]
    delta_long = radians(point_2[1] - point_1[1])
    acos_input = sin(radian_point_1[0]) * sin(radian_point_2[0]) + cos(radian_point_1[0]) * cos(radian_point_2[0]) * cos(delta_long)
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
