from scripts.models.body import Body
from scripts.models.movement import Movement


class Character(Body, Movement):
    def __init__(self):
        Body.__init__(self)
        Movement.__init__(self)

    def update(self):
        has_speed = self.speed > 0
        if has_speed:
            self.position.x += self.speed * self.direction.x
            self.position.y += self.speed * self.direction.y

    def __str__(self):
        Body.__str__(self)
        Movement.__str__(self)
        return (f"Character [ "
                f"{Body.__str__(self)} "
                f"{Movement.__str__(self)} "
                f"]"
                )
