from scripts.models.Element import Element


def collision_check(e1: Element, e2: Element):
    if (e1.position.x + e1.dimension.width) < e2.position.x or e1.position.x > (e2.position.x + e2.dimension.width):
        return False
    if (e1.position.y + e1.dimension.height) < e2.position.y or e1.position.y > (e2.position.y + e2.dimension.height):
        return False
    return True


def collider_bloc_ball(bloc: Element, ball: Element):
    ...
