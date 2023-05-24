from enum import Enum

from scripts.models.character import Character
from scripts.models.interactions import Interactions
from scripts.utils.mixins.selection_character import SelectionCharacterMixin


class BallType(Enum):
    basic_white = "ball_basic_white.png"


class Ball(Character, SelectionCharacterMixin(BallType).mixin, Interactions):
    def __init__(self):
        self._was_thrown = False
        super().__init__()

    def get_radius(self):
        return self.dimension.x / 2

    @classmethod
    def create_standard_ball(cls):
        return cls()

    @property
    def was_thrown(self):
        return self._was_thrown

    @was_thrown.setter
    def was_thrown(self, was_thrown: bool):
        self._was_thrown = was_thrown
