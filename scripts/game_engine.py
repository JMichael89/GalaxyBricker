import sys
import pygame

from scripts.scenes.game_play import GamePlay
from scripts.scenes.intro import Intro
from scripts.scenes.menu import Menu
from scripts.utils.levels import generate_level
from scripts.utils.window import Window


class GameEngine:
    def __init__(self):
        pygame.init()
        self.windows = Window(pygame, "Galaxy Bricker", 1200, 900)
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 20)
        self.FPS = 60

    def run(self):
        Intro.show(self.windows, self.clock)
        while True:
            menu = Menu(self.windows, self.clock)
            level = menu.show()
            gameplay = GamePlay(self.windows, self.clock, generate_level(level))
            gameplay.init()
