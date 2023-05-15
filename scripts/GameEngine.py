import os
from random import random
from turtle import delay

from scripts.characters.Ball import Ball, BallType
from scripts.characters.Platform import Platform, PlatformType
from scripts.models.Collider import collision_check
from scripts.utils.Vector import Vector
from scripts.utils.Window import Window
from scripts.utils.Dimension import Dimension

import pygame


class GameEngine:
    def __init__(self):
        self.pygame = pygame
        self.pygame.init()
        self.windows = Window(pygame, "Galaxy Bricker", Dimension(780, 600))

    def run(self):
        ball1 = Ball(Vector(10, 100), Dimension(15, 15))
        ball1.select_ball(BallType.basic_white)
        ball1.set_speed(random(), random())

        ball2 = Ball(Vector(100, 80), Dimension(15, 15))
        ball2.select_ball(BallType.basic_white)
        ball2.set_speed(random(), random())

        self.windows.add_element(ball1, ball2)

        game_is_active = True
        while game_is_active:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    game_is_active = False

            self.windows.update()
            update(self.windows, ball1, ball2)
            if collision_check(ball1, ball2):
                ball1.speed.multiplication(0)
                ball2.speed.multiplication(0)

        pygame.quit()


def update(windows, *elements):
    for element in elements:
        if (element.position.x + element.dimension.width) >= windows.dimension.width:
            element.speed.x *= -1
        elif element.position.x < 0:
            element.speed.x *= -1

        if (element.position.y + element.dimension.height) >= windows.dimension.height:
            element.speed.y *= -1
        elif element.position.y < 0:
            element.speed.y *= -1

