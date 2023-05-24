import math
import numbers

from scripts.utils.my_exception import MyException


class Interactions:
    def __init__(self):
        self._x_min = None
        self._x_max = None
        self._y_min = None
        self._y_max = None

    def restrict_area_of_movement(self, x_min: numbers, x_max: numbers, y_min: numbers, y_max: numbers):
        self._validate_range(x_min, x_max)
        self._validate_range(y_min, y_max)

        self._x_min = x_min
        self._x_max = x_max
        self._y_min = y_min
        self._y_max = y_max

        self.update = self._update

    @staticmethod
    def _validate_range(position_min, position_max):
        range_is_valid = position_min < position_max

        if not range_is_valid:
            raise MyException("The minimum position to be less than the maximum position")

    def _update(self):
        has_speed = self.speed > 0
        if has_speed:
            self._move_to_right()
            self._move_to_left()
            self._move_to_top()
            self._move_to_down()

    def _move_to_right(self):
        if self.direction.x > 0 and self._validate_move_to_right():
            self.position.x += self.speed

    def _move_to_left(self):
        if self.direction.x < 0 and self._validate_move_to_left():
            self.position.x -= self.speed

    def _move_to_top(self):
        if self.direction.y < 0 and self._validate_move_to_top():
            self.position.y -= self.speed

    def _move_to_down(self):
        if self.direction.y > 0 and self._validate_move_to_down():
            self.position.y += self.speed

    def _validate_move_to_left(self):
        move_is_valid_to_left = self.position.x > self._x_min if self._x_min is not None else None
        return move_is_valid_to_left

    def _validate_move_to_right(self):
        move_is_valid_to_right = self.position.x + self.get_width() < self._x_max if self._x_max is not None else None
        return move_is_valid_to_right

    def _validate_move_to_top(self):
        move_is_valid_to_down = self.position.y > self._y_min if self._y_min is not None else None
        return move_is_valid_to_down

    def _validate_move_to_down(self):
        move_is_valid_to_top = self.position.y + self.get_height() < self._y_max if self._y_max is not None else None
        return move_is_valid_to_top

    @staticmethod
    def check_collision(e1, e2):
        if (e1.position.x + e1.dimension.x) <= e2.position.x or e1.position.x >= (e2.position.x + e2.dimension.x):
            return False
        if (e1.position.y + e1.dimension.y) <= e2.position.y or e1.position.y >= (e2.position.y + e2.dimension.y):
            return False
        return True

    @staticmethod
    def distance_between(point1, point2):
        x1 = point1.x
        y1 = point1.y
        x2 = point2.x
        y2 = point2.y

        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        return distance

    @staticmethod
    def set_direction_result(ball, corner):
        direction_x = (ball.get_center().x - corner.x) / ball.get_radius()
        direction_y = (ball.get_center().y - corner.y) / ball.get_radius()
        direction = (direction_x, direction_y)

        ball.direction = direction
