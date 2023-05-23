import math
import numbers
from typing import Optional


class Vector:
    def __init__(self, x: Optional[numbers] = 0, y: Optional[numbers] = 0):
        self._x = x
        self._y = y

    def get_angle(self):
        angle_radius = math.atan2(self._y, self._x)
        angle_degrees = math.degrees(angle_radius)
        return angle_degrees

    def get_geometry(self):
        return f"{self._x}x{self._y}"

    def multiplication_by(self, module):
        self._x *= module
        self._y *= module

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        self._x = x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        self._y = y

    def __add__(self, other):
        x = self._x + other.x
        y = self._y + other.y
        return Vector(x, y)

    def __sub__(self, other):
        x = self._x - other.x
        y = self._y - other.y
        return Vector(x, y)

    def __mul__(self, module):
        return Vector(self._x * module, self._y * module)

    def __str__(self):
        return f"Vector [ x={self._x}, y={self._y} ]"
