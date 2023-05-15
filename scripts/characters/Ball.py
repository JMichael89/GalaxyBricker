import os
from enum import Enum

import pygame

from scripts.models.Element import Element
from scripts.utils.Dimension import Dimension


class BallType(Enum):
    basic_white = "ball_basic_white.png"


class Ball(Element):
    def select_ball(self, style: Enum):
        image = pygame.image.load("files/graphics/characters/"+style.value)
        self.update_image(image)
