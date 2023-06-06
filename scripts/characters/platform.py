from enum import Enum

from scripts.models.character import Character
from scripts.models.interactions import Interactions
from scripts.utils.mixins.selection_character import SelectionCharacterMixin


class PlatformType(Enum):
    animate1 = "platform1.png"


class Platform(Character, SelectionCharacterMixin(PlatformType).mixin, Interactions):
    def __init__(self, ):
        Character.__init__(self)
        Interactions.__init__(self)

    def move_to_left(self, window_size):
        if self.position.x > 0:
            self.direction.x = -1

    def move_to_right(self, window_size):
        if self.position.x + self.get_width() < window_size.x:
            self.direction.x = 1
