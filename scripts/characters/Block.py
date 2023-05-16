from enum import Enum

import pygame

from scripts.models.Element import Element


class BlockType(Enum):
    b1 = "bloc.png"


class Block(Element):
    def select_bloc(self, style: Enum):
        image = pygame.image.load("files/graphics/characters/"+style.value)
        self.update_image(image)
