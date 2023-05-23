import math

from scripts.characters.ball import Ball
from scripts.characters.block import Block
from scripts.models.body import Body
from scripts.utils.vector import Vector


class Interactions:
    def __init__(self):
        ...

    @staticmethod
    def check_collision(e1: Body, e2: Body):
        if (e1.position.x + e1.dimension.x) <= e2.position.x or e1.position.x >= (e2.position.x + e2.dimension.x):
            return False
        if (e1.position.y + e1.dimension.y) <= e2.position.y or e1.position.y >= (e2.position.y + e2.dimension.y):
            return False
        return True

    @staticmethod
    def check_external_collider(bloc: Body, ball: Ball):
        ...

    @staticmethod
    def collide_corner(bloc: Block, ball: Ball, ):
        ...

    @staticmethod
    def distance_between(point1: Vector, point2: Vector):
        x1 = point1.x
        y1 = point1.y
        x2 = point2.x
        y2 = point2.y

        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        return distance

    @staticmethod
    def set_direction_result(ball: Ball, corner: Vector):
        direction_x = (ball.get_center().x - corner.x) / ball.get_radius()
        direction_y = (ball.get_center().y - corner.y) / ball.get_radius()
        direction = Vector(direction_x, direction_y)

        ball.direction = direction
