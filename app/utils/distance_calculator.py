from config import SEARCH_RADIUS


def get_central_angle(point_1, point_2):
    # delta_lat = point_1[0] - point_2[0]
    delta_long = point_2[1] - point_2[1]
    # angle = arccos(sin(point_1[0])*sin(point_2[0]) + cos(point_2[1]) * cos(delta_long))
    return 0



def get_arc_length(point_1, point_2):
    return 0
    # radius = SEARCH_RADIUS
    # central_angle = get_central_angle(point_1, point_2)
    # return radius * central_angle