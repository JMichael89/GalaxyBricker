import pygame

from scripts.utils.Dimension import Dimension
from scripts.utils.Vector import Vector


class Element:
    def __init__(self, position: Vector = None, dimension: Dimension = None, image: pygame.image = None):
        self.position = position if position else Vector()
        self.dimension = dimension if dimension else Dimension()
        self.image = image if image else None
        self.direction = Vector()
        self.speed = 0
        self.speed_max = 1
        self.speed_min = 0

    def get_center(self):
        center_x = self.position.x + (self.dimension.x / 2)
        center_y = self.position.y + (self.dimension.y / 2)
        return Vector(center_x, center_y)

    def get_position(self):
        return self.position.x, self.position.y

    def get_width(self):
        return self.dimension.x

    def get_height(self):
        return self.dimension.y

    def update(self):
        if self.speed != 0:
            self.position.x += self.speed * self.direction.x
            self.position.y += self.speed * self.direction.y

    def update_image(self, image):
        self.image = pygame.transform.scale(image, (self.dimension.x, self.dimension.y))

    def set_position(self, x, y):
        self.position = Vector(x, y)

    def set_dimension(self, width, height):
        self.dimension = Dimension(width, height)

        if self.image:
            self.image = pygame.transform.scale(self.image, (self.dimension.x, self.dimension.y))

    def set_speed(self, speed):
        self.speed = speed

    def set_direction(self, x, y):
        if x > 1 or x < -1 or y > 1 or y < -1:
            raise Exception("direção deve ser entre -1 e 1")

        self.direction = Vector(x, y)

    def __str__(self):
        return f"Element [ " \
               f"position: {self.position}, " \
               f"dimension: {self.dimension}, " \
               f"speed: {self.speed}, " \
               f"speed_max: {self.speed_max}, " \
               f"speed_min: {self.speed_min}, " \
               f"image: {self.image} ]"
