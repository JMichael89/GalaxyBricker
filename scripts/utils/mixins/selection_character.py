from enum import Enum
from typing import Type

import pygame


class SelectionCharacterMixin:
    def __init__(self, enum_type: Type[Enum]):
        self.enum_type = enum_type

    @property
    def mixin(self):
        enum_type = self.enum_type

        class Mixin:
            def select_character(self, style: enum_type):
                self.image = pygame.image.load(f"files/graphics/characters/{style.value}")

        return Mixin
