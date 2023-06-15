import numbers
from typing import Optional

from scripts.utils.my_exception import MyException
from scripts.utils.vector import Vector


class Movement:
    def __init__(self, direction: Optional[Vector] = None, speed: Optional[numbers] = 0):
        self._direction = direction if direction else Vector()
        self._speed = speed if speed else 0

    def update(self):
        has_speed = self.speed > 0
        if has_speed:
            self.position.x += self.speed * self.direction.x
            self.position.y += self.speed * self.direction.y

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, speed):
        self._speed = speed

    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, direction: Vector):
        x = self.limit_of_1(direction.x)
        y = self.limit_of_1(direction.y)
        self._direction = Vector(x, y)

    def set_direction(self, x, y):
        self.direction = Vector(x, y)

    @staticmethod
    def limit_of_1(valor):
        if 1 < valor or valor < -1:
            valor = 1 if valor > 1 else -1
        return valor

    def __str__(self):
        return (
            f"Movement [ "
            f"Direction {self._direction} "
            f"Speed {self._speed} "
            f" ]"
        )
