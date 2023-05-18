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
            print(intersection_area)

    if intersection_area.__len__() == 2:
        tratar_colisao_quina_bloco(bloc, ball, intersection_area)
        ...

    elif intersection_area.__len__() == 1:
        if intersection_area[0] == "Top" or intersection_area[0] == "Down":
            ball.speed.y *= -1
        if intersection_area[0] == "Left" or intersection_area[0] == "Right":
            ball.speed.x *= -1

    return intersection_area


def tratar_colisao_quina_bloco(bloc: Element, ball: Ball, intersection_area):
    ...

