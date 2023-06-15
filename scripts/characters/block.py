from enum import Enum

import pygame

from scripts.models.character import Character
from scripts.utils.interactions import Interactions
from scripts.utils.mixins.selection_character import SelectionCharacterMixin


class BlockType(Enum):
    b1 = "bloc.png"


class Block(Character, SelectionCharacterMixin(BlockType).mixin, Interactions):
    def __init__(self):
        super().__init__()
        self.life = 1

    def select_bloc(self, style: Enum):
        self.life = 100
        image = pygame.image.load("files/graphics/characters/"+style.value)
        self.update_image(image)

    def hit(self, hit):
        self.life -= hit
        if self.life <= 0:
            return True

