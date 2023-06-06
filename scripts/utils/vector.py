import math
import numbers
from typing import Optional


class Vector:
    def __init__(self, x: Optional[numbers] = 0, y: Optional[numbers] = 0):
        self._x = x
        self._y = y

    def get_angle(self):
        angle_radius = math.atan2(self.y, self.x)
        angle_degrees = math.degrees(angle_radius)
        return angle_degrees

    def get_geometry(self):
        return f"{self.x}x{self.y}"

    def multiplication_by(self, module):
        self.x *= module
        self.y *= module

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
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Vector(x, y)

    def __mul__(self, other):
        return Vector(self.x * other.x, self.y * other.y)

    def __str__(self):
        return f"Vector [ x={self.x}, y={self.y} ]"
