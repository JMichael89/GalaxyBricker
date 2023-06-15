import sys
import pygame

from scripts.utils.animation import Animation
from scripts.utils.vector import Vector
from scripts.utils.window import Window


class Intro:
    @staticmethod
    def show(window: Window, clock):
        Intro._opening(window, clock)

        logo = Animation("files/graphics/logo/logo4.gif")
        logo.dimension = Vector(window.width, window.height)
        window.add_element(logo)

        start = Animation("files/graphics/logo/start_i.gif")
        start.dimension = Vector(window.width, window.height)
        start.position = Vector(0, -100)
        start.continuos = False
        window.add_element(start)

        while True:
            if Intro._listen_keyboard():
                window.fade_transition(clock)
                window.restart()
                break

            if not start.update_frame():
                window.remove_element(start)
                start = Animation("files/graphics/logo/start_f.gif")
                start.set_dimension(window.width, window.height)
                start.set_position(0, -100)
                window.add_element(start)

            logo.update_frame()
            clock.tick(5)
            window.update()

    @staticmethod
    def _listen_keyboard():
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

    @staticmethod
    def _opening(window: Window, clock):
        logo_animate = Animation("files/graphics/logo/animação de abertura.gif")
        logo_animate.dimension = Vector(window.width, window.height)
        logo_animate.continuos = False
        window.add_element(logo_animate)

        while True:
            if Intro._listen_keyboard():
                window.restart()
                break

            clock.tick(5)
            window.update()

            if not logo_animate.update_frame():
                window.restart()
                break
