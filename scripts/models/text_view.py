from typing import Optional, Union

import pygame

from scripts.models.element import Element
from scripts.utils.vector import Vector


class TextView(Element):
    def __init__(self, text, font_style, font_size, color):
        super().__init__()
        self.text = text
        self.font_size = font_size
        self.color = color
        self.font = pygame.font.SysFont(font_style, self.font_size)
        self.surface = self.font.render(self.text, True, self.color)
        self.rect = self.surface.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    def set_position(self, x, y):
        super().set_position(x, y)
        self.rect.x = x
        self.rect.y = y

    def position_in_center(self, screen_width, screen_height):
        self.rect.centerx = screen_width // 2
        self.rect.centery = screen_height // 2
