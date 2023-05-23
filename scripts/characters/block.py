from enum import Enum

import pygame

from scripts.models.character import Character
from scripts.utils.mixins.selection_character import SelectionCharacterMixin


class BlockType(Enum):
    b1 = "bloc.png"


class Block(Character, SelectionCharacterMixin(BlockType).mixin):
    def select_bloc(self, style: Enum):
        image = pygame.image.load("files/graphics/characters/"+style.value)
        self.update_image(image)
