import math


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Vector(x, y)

    def multiplication(self, mul):
        self.x *= mul
        self.y *= mul

    def angle(self):
        angle_rad = math.atan2(self.y, self.x)
        angle_deg = math.degrees(angle_rad)
        return angle_deg

    def __str__(self):
        return f"Vector [ x={self.x}, y={self.y} ]"
