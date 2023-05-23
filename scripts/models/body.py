from typing import Optional

import pygame

from scripts.utils.my_exception import MyException
from scripts.utils.vector import Vector


class Body:
    def __init__(self, position: Optional[Vector] = None, dimension: Vector = None, image: pygame.image = None):
        self._position = position if position else Vector()
        self._dimension = dimension if dimension else Vector()
        self._image = image if image else None

    def get_center(self):
        center_x = self._position.x + (self._dimension.x / 2)
        center_y = self._position.y + (self._dimension.y / 2)
        return Vector(center_x, center_y)

    def get_width(self):
        return self._dimension.x

    def get_height(self):
        return self._dimension.y

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, image):
        self._validate_image(image)
        self._image = pygame.transform.scale(image, (self._dimension.x, self._dimension.y))

    @staticmethod
    def _validate_image(image):
        image_is_valid = isinstance(image, pygame.Surface)

        if not image_is_valid:
            raise MyException("This image is not valid")

    @property
    def dimension(self):
        return self._dimension

    @dimension.setter
    def dimension(self, dimension):
        self._dimension = dimension
        self._image = self._image

    def set_dimension(self, width, height):
        self._dimension = Vector(width, height)
        self._image = self._image

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, position):
        self._position = position

    def set_position(self, x, y):
        self._position = Vector(x, y)

    def __str__(self):
        return (
            f"Body [ "
            f"Position {self._position} "
            f"Dimension {self._dimension} "
            f"Image {self._image} "
            f"]"
                )
