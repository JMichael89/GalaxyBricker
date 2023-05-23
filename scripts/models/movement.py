import numbers
from typing import Optional

from scripts.utils.my_exception import MyException
from scripts.utils.vector import Vector


class Movement:
    def __init__(self, direction: Optional[Vector] = None, speed: Optional[numbers] = 0,
                 speed_max: Optional[numbers] = 0, speed_min: Optional[numbers] = 0):
        self._direction = direction if direction else Vector()
        self._speed = speed if speed else 0
        self._speed_max = speed_max if speed_max else 1
        self._speed_min = speed_min if speed_min else 0

    def set_range_speed(self, speed_min, speed_max):
        self._validate_range_speed(speed_min, speed_max)
        self._speed_min = speed_min
        self._speed_max = speed_max

    @staticmethod
    def _validate_range_speed(speed_min, speed_max):
        range_is_valid = speed_min >= speed_max

        if not range_is_valid:
            raise MyException("The minimum speed to be less than the maximum speed")

    @property
    def speed_max(self):
        return self._speed_max

    @speed_max.setter
    def speed_max(self, speed_max):
        self._validate_speed_max(speed_max)
        self._speed_max = speed_max

    def _validate_speed_max(self, speed_max):
        speed_max_is_valid = speed_max >= self._speed_min

        if not speed_max_is_valid:
            raise MyException("Max speed cannot be less than min speed")

    @property
    def speed_min(self):
        return self._speed_min

    @speed_min.setter
    def speed_min(self, speed_min):
        self._validate_speed_min(speed_min)
        self._speed_min = speed_min

    def _validate_speed_min(self, speed_min):
        speed_min_is_valid = speed_min <= self._speed_max

        if not speed_min_is_valid:
            raise MyException("Minimum speed cannot be greater than the maximum speed.")

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, speed):
        self._validate_speed(speed)
        self._speed = speed

    def _validate_speed(self, speed):
        speed_is_valid = self._speed_min <= speed <= self._speed_max

        if not speed_is_valid:
            raise MyException("Speed is outside the min and max ranges")

    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, direction: Vector):
        self._validate_directions(direction.x, direction.y)
        self._direction = direction

    def set_direction(self, x, y):
        self._validate_directions(x, y)
        self._direction = Vector(x, y)

    @staticmethod
    def _validate_directions(x, y):
        x_is_valid = -1 <= x <= 1
        y_is_valid = -1 <= y <= 1

        if not x_is_valid or not y_is_valid:
            raise MyException("direction must be between -1 and 1")

    def __str__(self):
        return (
            f"Movement [ "
            f"Direction {self._direction} "
            f"Speed {self._speed} "
            f"Speed_min {self._speed_min} "
            f"Speed_max {self._speed_max} "
            f" ]"
        )
