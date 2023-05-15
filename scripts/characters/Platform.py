from enum import Enum

import pygame

from scripts.models.Element import Element


class PlatformType(Enum):
    animate1 = "platform1.png"
    animate2 = "plataforma_animate1.gif"


class Platform(Element):
    def select_platform(self, style: Enum):
        image = pygame.image.load("files/graphics/characters/"+style.value)
        self.update_image(image)
