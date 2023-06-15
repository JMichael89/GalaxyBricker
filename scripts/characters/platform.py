from enum import Enum

from scripts.models.character import Character
from scripts.utils.interactions import Interactions
from scripts.utils.mixins.selection_character import SelectionCharacterMixin


class PlatformType(Enum):
    animate1 = "platform1.png"


class Platform(Character, SelectionCharacterMixin(PlatformType).mixin, Interactions):
    def __init__(self, ):
        Character.__init__(self)
        Interactions.__init__(self)

    def move_to_left(self, width):
        if self.position.x > 0:
            self.direction.x = -1

    def move_to_right(self, width):
        if self.position.x + self.get_width() < width:
            self.direction.x = 1
