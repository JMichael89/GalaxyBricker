import pygame

from scripts.models.character import Character
from scripts.models.text_view import TextView
from scripts.utils.animation import Animation


class Window:
    def __init__(self, instance, title: str, width, height):
        self.title = title
        self.width = width
        self.height = height

        self.display = instance.display
        self.screen = self.display.set_mode((width, height))
        pygame.display.set_caption("Galaxy Bricker")
        self.elements = []

    def update(self):
        self.screen.fill((0, 0, 0))
        for element in self.elements:
            if isinstance(element, Character):
                if element.image is not None:
                    element.update()
                    self.screen.blit(element.image, (element.position.x, element.position.y))

            elif isinstance(element, Animation):
                self.screen.blit(element.frame, (element.position.x, element.position.y))

            elif isinstance(element, TextView):
                self.screen.blit(element.surface, element.rect)

        self.display.update()

    def fade_transition(self, clock):
        fade_img = pygame.Surface((self.width, self.height)).convert_alpha()
        fade = fade_img.get_rect()
        fade_img.fill("black")
        fade_alpha = 0

        while True:
            fade_alpha += 10
            fade_img.set_alpha(fade_alpha)
            self.screen.blit(fade_img, fade)
            clock.tick(20)
            self.display.flip()
            if fade_alpha >= 255:
                break

    def add_element(self, *elements):
        for element in elements:
            self.elements.append(element)

    def remove_element(self, *elements):
        for element in elements:
            if element in self.elements:
                self.elements.remove(element)

    def restart(self):
        self.elements.clear()
