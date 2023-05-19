import math

from scripts.characters.Ball import Ball
from scripts.models.Element import Element
from scripts.utils.Vector import Vector


def check_collision(e1: Element, e2: Element):
    if (e1.position.x + e1.dimension.x) <= e2.position.x or e1.position.x >= (e2.position.x + e2.dimension.x):
        return False
    if (e1.position.y + e1.dimension.y) <= e2.position.y or e1.position.y >= (e2.position.y + e2.dimension.y):
        return False
    return True


def check_external_collider(bloc: Element, ball: Ball):
    intersection_area = []
    if bloc.position.y - ball.get_radius() <= ball.get_center().y < bloc.position.y + bloc.get_height() + ball.get_height():
        if bloc.position.x - ball.get_radius() <= ball.get_center().x < bloc.position.x:
            intersection_area.append("Left")

        elif bloc.position.x + bloc.get_width() < ball.get_center().x <= bloc.position.x + bloc.get_width() + ball.get_radius():
            intersection_area.append("Right")

    if bloc.position.x - ball.get_radius() <= ball.get_center().x < bloc.position.x + bloc.get_width() + ball.get_width():
        if bloc.position.y - ball.get_radius() <= ball.get_center().y < bloc.position.y:
            intersection_area.append("Top")

        elif bloc.position.y + bloc.get_height() < ball.get_center().y <= bloc.position.y + bloc.get_height() + ball.get_radius():
            intersection_area.append("Down")

    if intersection_area.__len__() == 1:
        collider = intersection_area[0]

        if collider == "Top" or collider == "Down":
            ball.direction.y *= -1
            ball.direction.x += bloc.direction.x * 0.25
        if collider == "Left" or collider == "Right":
            ball.direction.x *= -1
            ball.direction.y += bloc.direction.y * 0.25

        return True

    elif intersection_area.__len__() == 2:
        collider = collide_corner(bloc, ball, intersection_area)

        if collider:
            return True


def collide_corner(bloc: Element, ball: Ball, intersection_area):
    collider = None
    corner = None

    if intersection_area[1] == "Down":
        if intersection_area[0] == "Right":
            corner = Vector(bloc.position.x + bloc.get_width(), bloc.position.y + bloc.get_height())
            distance_to_center = distance_between(corner, ball.get_center())

            if ball.get_radius() >= distance_to_center:
                collider = "Down/Right"

        else:
            corner = Vector(bloc.position.x, bloc.position.y + bloc.get_height())
            distance_to_center = distance_between(corner, ball.get_center())

            if ball.get_radius() >= distance_to_center:
                collider = "Down/Left"

    elif intersection_area[1] == "Top":
        if intersection_area[0] == "Right":
            corner = Vector(bloc.position.x + bloc.get_width(), bloc.position.y)
            distance_to_center = distance_between(corner, ball.get_center())

            if ball.get_radius() >= distance_to_center:
                collider = "Top/Right"

        else:
            corner = Vector(bloc.position.x, bloc.position.y)
            distance_to_center = distance_between(corner, ball.get_center())

            if ball.get_radius() >= distance_to_center:
                collider = "Top/Left"

    if collider:
        set_direction_result(ball, corner)
        return True


def distance_between(point1: Vector, point2: Vector):
    x1 = point1.x
    y1 = point1.y
    x2 = point2.x
    y2 = point2.y

    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance


def set_direction_result(ball: Ball, corner: Vector):
    direction_x = (ball.get_center().x - corner.x) / ball.get_radius()
    direction_y = (ball.get_center().y - corner.y) / ball.get_radius()
    direction = Vector(direction_x, direction_y)

    ball.direction = direction
