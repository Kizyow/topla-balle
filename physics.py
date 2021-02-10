import math
from vector import Vector


def angle(start_vector, end_vector):
    x = end_vector.get_x() - start_vector.get_x()
    y = end_vector.get_y() - start_vector.get_y()
    return math.atan2(y, x)


def distance(start_vector, end_vector):
    x = end_vector.get_x() - start_vector.get_x()
    y = end_vector.get_y() - start_vector.get_y()
    return math.sqrt(x ** 2 + y ** 2)


def position(theta, size, center=Vector()):
    x = math.cos(theta) * size + center.get_x()
    y = math.sin(theta) * size + center.get_y()
    return Vector(x, y)
