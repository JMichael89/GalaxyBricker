from enum import Enum

from scripts.models.character import Character
from scripts.utils.mixins.selection_character import SelectionCharacterMixin


class BossType(Enum):
    b1 = "bloc.png"


class Boss(Character, SelectionCharacterMixin(BossType).mixin):
    ...
