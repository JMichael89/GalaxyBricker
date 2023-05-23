from enum import Enum

from scripts.models.character import Character
from scripts.utils.mixins.selection_character import SelectionCharacterMixin


class BallType(Enum):
    basic_white = "ball_basic_white.png"


class Ball(Character, SelectionCharacterMixin(BallType).mixin):
    def __init__(self):
        super().__init__()
        ...

    def get_radius(self):
        return self.dimension.x / 2

    @classmethod
    def create_standard_ball(cls):
        return cls()
