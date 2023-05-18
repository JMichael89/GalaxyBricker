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
        print(collider)

        if collider == "Top" or collider == "Down":
            ball.direction.y *= -1
        if collider == "Left" or collider == "Right":
            ball.direction.x *= -1

        return collider

    elif intersection_area.__len__() == 2:
        collider = collide_corner(bloc, ball, intersection_area)

        if collider:
            print(collider)
            return collider


def collide_corner(bloc: Element, ball: Ball, intersection_area):
    collider = None
    cornner = None
    cornner_centerball = None

    if intersection_area[1] == "Down":
        if intersection_area[0] == "Right":
            cornner = Vector(bloc.position.x + bloc.get_width(), bloc.position.y + bloc.get_height())
            cornner_centerball = distance_between(cornner, ball.get_center())

            if ball.get_radius() >= cornner_centerball:
                collider = "Down/Right"

        else:
            cornner = Vector(bloc.position.x, bloc.position.y + bloc.get_height())
            cornner_centerball = distance_between(cornner, ball.get_center())

            if ball.get_radius() >= cornner_centerball:
                collider = "Down/Left"

    elif intersection_area[1] == "Top":
        if intersection_area[0] == "Right":
            cornner = Vector(bloc.position.x + bloc.get_width(), bloc.position.y)
            cornner_centerball = distance_between(cornner, ball.get_center())

            if ball.get_radius() >= cornner_centerball:
                collider = "Top/Right"

        else:
            cornner = Vector(bloc.position.x, bloc.position.y)
            cornner_centerball = distance_between(cornner, ball.get_center())

            if ball.get_radius() >= cornner_centerball:
                collider = "Top/Left"

    if collider:
        print(collider)
        test(ball, cornner)
        return collider


def distance_between(point1: Vector, point2: Vector):
    x1 = point1.x
    y1 = point1.y
    x2 = point2.x
    y2 = point2.y

    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance


def alterar_direcao_velocidade_bola(corner: Vector, ball_center: Vector, ball_speed: Vector, d):
    quina_x = corner.x
    quina_y = corner.y
    bola_centro_x = ball_center.x
    bola_centro_y = ball_center.y
    velocidade_x = ball_speed.x
    velocidade_y = ball_speed.y

    vetor_quina = (quina_x - bola_centro_x, quina_y - bola_centro_y)
    comprimento_vetor_quina = d
    direcao_quina = (vetor_quina[0] / comprimento_vetor_quina, vetor_quina[1] / comprimento_vetor_quina)

    produto_escalar = direcao_quina[0] * velocidade_x + direcao_quina[1] * velocidade_y

    reflexao_x = -1 * produto_escalar * direcao_quina[0] - velocidade_x
    reflexao_y = -1 * produto_escalar * direcao_quina[1] - velocidade_y
    reflexao = Vector(reflexao_x, reflexao_y)

    return reflexao


def test(ball: Ball, cornner: Vector):
    print("Tests:")
    print("cornner          :", cornner)
    print("ball.center      :", ball.get_center())
    print("ball.radius      :", ball.get_radius())

    direction_x = (ball.get_center().x - cornner.x)/ball.get_radius()
    direction_y = (ball.get_center().y - cornner.y)/ball.get_radius()
    direction = Vector(direction_x, direction_y)

    print("direction_x         :", direction_x)
    print("direction_y         :", direction_y)
    print("ball.speed          :", ball.speed)
    print("direction           :", direction)

    ball.direction = direction
