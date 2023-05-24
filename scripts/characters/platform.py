from enum import Enum

from scripts.models.character import Character
from scripts.models.interactions import Interactions
from scripts.utils.mixins.selection_character import SelectionCharacterMixin


class PlatformType(Enum):
    animate1 = "platform1.png"


class Platform(Character, SelectionCharacterMixin(PlatformType).mixin, Interactions):
    def __init__(self,):
        Character.__init__(self)
        Interactions.__init__(self)

    def move_to_left(self):
        if self._validate_move_to_left():
            self.direction.x = -1

    def move_to_right(self):
        if self._validate_move_to_right():
            self.direction.x = 1
