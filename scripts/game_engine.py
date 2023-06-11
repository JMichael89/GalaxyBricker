import sys
import pygame

from scripts.scenes.menu import Menu
from scripts.utils.window import Window


class GameEngine:
    def __init__(self):
        pygame.init()
        self.windows = Window(pygame, "Galaxy Bricker", 800, 600)
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 20)
        self.FPS = 60

    def run(self):
        Menu.show_menu(self.windows, self.clock)
        print("opaa")
        self.windows.update()

        while True:
            self.clock.tick(self.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.windows.update()

