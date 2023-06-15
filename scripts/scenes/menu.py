import sys

import pygame

from scripts.models.text_view import TextView
from scripts.utils.levels import levels
from scripts.utils.window import Window


class Menu:
    def __init__(self, window: Window, clock):
        self.window = window
        self.clock = clock
        self.point = None
        self.options = []
        self.selection = 0

    def show(self):
        self.point = TextView(">", "Arial", 40, (0, 255, 0))
        self.point.set_position(75, 50)

        self.options = self.create_options()

        self.window.add_element(self.point, *self.options)

        while True:
            if self._listen_keyboard():
                self.window.fade_transition(self.clock)
                self.window.restart()
                return self.selection

            self.clock.tick(5)
            self.window.update()

    def _listen_keyboard(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return True
                elif event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_UP:
                    self.update_selection(-1)
                    self.clock.tick(50)
                elif event.key == pygame.K_DOWN:
                    self.update_selection(1)
                    self.clock.tick(50)

    def create_options(self):
        options = []
        for i in range(len(levels)):
            option1 = TextView(levels[i]["name"], "Arial", 40, (0, 255, 0))
            option1.set_position(100, (i+1)*50)
            options.append(option1)

        return options

    def update_selection(self, acrescent):
        self.selection += acrescent
        if len(self.options) <= self.selection or self.selection < 0:
            self.selection += -acrescent

        self.update_selection_position()

    def update_selection_position(self):
        self.point.set_position(75, self.options[self.selection].position.y)
