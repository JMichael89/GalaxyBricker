from enum import Enum

from scripts.models.character import Character
from scripts.utils.mixins.selection_character import SelectionCharacterMixin


class PlatformType(Enum):
    animate1 = "platform1.png"


class Platform(Character, SelectionCharacterMixin(PlatformType).mixin):
    def __init__(self):
        super().__init__()
        ...

    def set_position(self, x, y):
        super().set_position(x, y)

    def update(self):
        if self.speed != 0:
            self.position.x += self.speed * self.direction.x
            self.position.y += self.speed * self.direction.y

