from scripts.models.Element import Element
from scripts.utils.Vector import Vector


def collision_check(e1: Element, e2: Element):
    if (e1.position.x + e1.dimension.width) < e2.position.x or e1.position.x > (e2.position.x + e2.dimension.width):
        return False
    if (e1.position.y + e1.dimension.height) < e2.position.y or e1.position.y > (e2.position.y + e2.dimension.height):
        return False
    return True


def collider_bloc_ball_update(bloc: Element, ball: Element):
    forca_reacao = None
    intersection_area = ""
    if ball.position.x <= bloc.position.x + bloc.dimension.width and \
            ball.position.x + ball.dimension.width >= bloc.position.x:
        if ball.position.y <= bloc.position.y + bloc.dimension.height:
            intersection_area = "em baixo"
        else:
            intersection_area = "em cima"
    else:
        if ball.position.y :
            ...


def collider_bloc_ball(bloc: Element, ball: Element):
    forca_reacao = Vector(0, 0)
    intersection_area = ""
    if (ball.position.y + 1 >= bloc.position.y + bloc.dimension.height) and \
            (ball.position.x >= bloc.position.x - (ball.dimension.width / 2)) and \
            (ball.position.x <= bloc.position.x + bloc.dimension.width - (ball.dimension.width / 2)):
        ball.speed.y *= -1
        intersection_area = "A1"

    elif (ball.position.x + 1 >= bloc.position.x + bloc.dimension.width) and \
            (ball.position.y >= bloc.position.y - (ball.dimension.height / 2)) and \
            (ball.position.y <= bloc.position.y + bloc.dimension.height - (ball.dimension.height / 2)):
        ball.speed.x *= -1
        intersection_area = "A2"

    elif (ball.position.y + ball.dimension.height - 1 <= bloc.position.y) and \
            (ball.position.x <= bloc.position.x + bloc.dimension.width - (ball.dimension.width / 2)) and \
            (ball.position.x >= bloc.position.x - (ball.dimension.width / 2)):
        ball.speed.y *= -1
        intersection_area = "A3"

    elif (ball.position.x + ball.dimension.width - 1 <= bloc.position.x) and \
            (ball.position.y >= bloc.position.y - (ball.dimension.height / 2)) and \
            (ball.position.y <= bloc.position.y + bloc.dimension.height - (ball.dimension.height / 2)):
        ball.speed.x *= -1
        intersection_area = "A4"
    else:
        ball.speed.x *= -1
        ball.speed.y *= -1
        intersection_area = "E"

    return intersection_area
