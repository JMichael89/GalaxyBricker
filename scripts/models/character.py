from scripts.models.element import Element
from scripts.models.movement import Movement


class Character(Element, Movement):
    def __init__(self):
        Element.__init__(self)
        Movement.__init__(self)
        self._animation = None

    @property
    def animation(self):
        return self._animation

    @animation.setter
    def animation(self, animation):
        self._animation = animation
        self._animation.set_dimension(self.dimension.x, self.dimension.y)
        self._animation.set_position(self.position.x, self.position.y)

    def __str__(self):
        Element.__str__(self)
        Movement.__str__(self)
        return (f"Character [ "
                f"{Element.__str__(self)} "
                f"{Movement.__str__(self)} "
                f"]"
                )
