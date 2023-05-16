import pygame

from scripts.utils.Dimension import Dimension
from scripts.utils.Vector import Vector


class Element:
    def __init__(self, position: object = None, dimension: object = None, image: object = None) -> object:
        self.position = position if position else Vector()
        self.dimension = dimension if dimension else Dimension()
        self.image = image if image else None
        self.speed = Vector()
        self.acceleration = Vector()
        self.speed_max = 0
        self.speed_min = 0

    def update(self):
        if self.acceleration != 0:
            self.speed += self.acceleration

        if self.speed != 0:
            self.position += self.speed

    def update_image(self, image):
        self.image = pygame.transform.scale(image, (self.dimension.width, self.dimension.height))

    def set_position(self, x, y):
        self.position = Vector(x, y)

    def set_dimension(self, width, height):
        self.dimension = Dimension(width, height)

        if self.image:
            self.image = pygame.transform.scale(self.image, (self.dimension.width, self.dimension.height))

    def set_speed(self, x, y):
        self.speed = Vector(x, y)

    def set_acceleration(self, x, y):
        self.acceleration = Vector(x, y)

    def __str__(self):
        return f"Element [ "\
               f"position: {self.position}, " \
               f"dimension: {self.dimension}, " \
               f"speed: {self.speed}, " \
               f"acceleration: {self.acceleration}, " \
               f"speed_max: {self.speed_max}, " \
               f"speed_min: {self.speed_min}, " \
               f"image: {self.image} ]"
