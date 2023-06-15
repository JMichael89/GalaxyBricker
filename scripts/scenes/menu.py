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
        self.options = self.create_options()

        self.point = TextView(">", "Arial", int(self.window.width * 0.05), (0, 255, 0))
        self.update_selection_position()
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

                elif event.key == pygame.K_DOWN:
                    self.update_selection(1)

    def create_options(self):
        options = []
        for i in range(len(levels)):
            option1 = TextView(levels[i]["name"], "Arial", int(self.window.height * 0.05), (0, 255, 0))
            option1.set_position(int(self.window.height * 0.1), (i+1)*int(self.window.height * 0.05))
            options.append(option1)

        return options

    def update_selection(self, acrescent):
        self.selection += acrescent
        if len(self.options) <= self.selection or self.selection < 0:
            self.selection += -acrescent

        self.update_selection_position()

    def update_selection_position(self):
        self.point.set_position(int(self.window.height * 0.05), self.options[self.selection].position.y)
