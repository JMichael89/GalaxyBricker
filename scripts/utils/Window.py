from tkinter import StringVar, Radiobutton, Tk
import pygame
from configs import configs
from scripts.models.Element import Element
from scripts.utils.Dimension import Dimension


class Window:
    def __init__(self, instance, title: str, dimension: Dimension):
        self.title = title
        self.dimension = dimension

        self.display = instance.display
        self.paint = self.display.set_mode((dimension.x, dimension.y))
        pygame.display.set_caption("Galaxy Bricker")
        self.elements = []

    def update(self):
        self.paint.fill((0, 0, 0))

        for element in self.elements:
            if element.image is not None:
                element.update()
                self.paint.blit(element.image, (element.position.x, element.position.y))

        self.display.flip()

    def add_element(self, *elements):
        for element in elements:
            self.elements.append(element)

    def remove_element(self, *elements):
        for element in elements:
            self.elements.remove(element)
