from enum import Enum

from scripts.models.character import Character
from scripts.models.interactions import Interactions
from scripts.utils.mixins.selection_character import SelectionCharacterMixin
from scripts.utils.vector import Vector


class BallType(Enum):
    basic_white = "ball_basic_white.png"


class Ball(Character, SelectionCharacterMixin(BallType).mixin, Interactions):
    def __init__(self):
        self._was_thrown = False
        super().__init__()

    def calculate_result_direction(self, element):
        self._calculate_result_direction(self, element)

    def check_collider_by_window(self, window):
        if self.position.x <= 0 or self.position.x + self.get_width() >= window.width:
            self.direction *= Vector(-1, 1)

        if self.position.y <= 0:
            self.direction *= Vector(1, -1)

    def check_collide(self, element: Character):
        return self._check_collision(self, element)

    def check_die(self, window):
        return self.position.y >= window.height

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
