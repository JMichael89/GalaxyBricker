import math

from scripts.utils.vector import Vector


class Interactions:
    def __init__(self):
        self._x_min = None
        self._x_max = None
        self._y_min = None
        self._y_max = None

    @staticmethod
    def _check_collision(e1, e2):
        if (e1.position.x + e1.dimension.x) <= e2.position.x or e1.position.x >= (e2.position.x + e2.dimension.x):
            return False
        if (e1.position.y + e1.dimension.y) <= e2.position.y or e1.position.y >= (e2.position.y + e2.dimension.y):
            return False
        return Interactions._calculate_result_direction(e1, e2)

    @staticmethod
    def _calculate_result_direction(ball, block):
        distance_x = ball.get_center().x - block.get_center().x
        distance_y = ball.get_center().y - block.get_center().y

        half_width = block.get_width() / 2
        half_height = block.get_height() / 2

        collision_side = abs(distance_x) > half_width
        collision_top_down = abs(distance_y) > half_height

        if collision_side and collision_top_down:
            corner_x = block.get_center().x + (half_width if distance_x > 0 else -half_width)
            corner_y = block.get_center().y + (half_height if distance_y > 0 else -half_height)

            normal_x = ball.get_center().x - corner_x
            normal_y = ball.get_center().y - corner_y
            normal_length = math.sqrt(normal_x ** 2 + normal_y ** 2)

            if normal_length <= ball.get_radius():
                normal_x /= normal_length
                normal_y /= normal_length

                dot_product = ball.direction.x * normal_x + ball.direction.y * normal_y

                direction_x = -2 * dot_product * normal_x
                direction_y = -2 * dot_product * normal_y

                ball.direction += Vector(direction_x, direction_y)

                if 0 >= ball.direction.y >= -0.1:
                    ball.direction.y = -0.1
                elif 0 <= ball.direction.y <= 0.1:
                    ball.direction.y = 0.1
                return True

        elif collision_side:
            ball.direction.x *= -1
            return True

        elif collision_top_down:
            ball.direction.y *= -1
            return True

        return False