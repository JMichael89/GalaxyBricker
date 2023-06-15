from scripts.models.element import Element
from scripts.models.movement import Movement


class Character(Element, Movement):
    def __init__(self):
        Element.__init__(self)
        Movement.__init__(self)

    def __str__(self):
        Element.__str__(self)
        Movement.__str__(self)
        return (f"Character [ "
                f"{Element.__str__(self)} "
                f"{Movement.__str__(self)} "
                f"]"
                )
