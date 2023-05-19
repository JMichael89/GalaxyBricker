from enum import Enum

import pygame

from scripts.characters.Ball import Ball
from scripts.models.Element import Element
from scripts.utils.Dimension import Dimension
from scripts.utils.Vector import Vector


class PlatformType(Enum):
    animate1 = "platform1.png"


class Platform(Element):
    def __init__(self, position: Vector = None, dimension: Dimension = None, image: pygame.image = None, ball: Ball = None):
        super().__init__(position, dimension, image)
        self.ball = ball

    def select_platform(self, style: Enum):
        image = pygame.image.load("files/graphics/characters/" + style.value)
        self.update_image(image)

    def update_ball(self, ball: Ball):
        self.ball = ball

    def set_position(self, x, y):
        super().set_position(x, y)
        self.movement_ball()

    def update(self):
        if self.speed != 0:
            self.position.x += self.speed * self.direction.x
            self.position.y += self.speed * self.direction.y
            self.movement_ball()

    def movement_ball(self):
        if self.ball:
            x1 = self.get_center().x - self.ball.get_radius()
            y1 = self.position.y - self.ball.get_height()
            self.ball.set_position(x1, y1)

    def throw_ball(self):
        if self.ball:
            self.ball.direction.y = 1
            self.ball.direction.x = self.direction.x
            self.ball.speed = self.ball.speed_max
            self.ball = None
