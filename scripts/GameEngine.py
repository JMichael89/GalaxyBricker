from random import random

from scripts.characters.Ball import Ball, BallType
from scripts.characters.Block import Block, BlockType
from scripts.characters.Platform import Platform, PlatformType
from scripts.models.Collider import collision_check, collider_bloc_ball
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
        ball1 = Ball(dimension=Dimension(20, 20))
        ball1.select_ball(BallType.basic_white)

        '''
        # Tsts A1
        ball1.set_position(290, 500)
        ball1.set_position(490, 500)
        ball1.set_speed(0, -0.5)
        
        # Tests A2
        ball1.set_position(600, 190)
        ball1.set_position(600, 390)
        ball1.set_speed(-0.5, 0)
        
        # Tests A3
        ball1.set_position(290, 0)
        ball1.set_position(490, 0)
        ball1.set_speed(0, 0.5)
        
        # Tests A4
        ball1.set_position(0, 190)
        ball1.set_position(0, 390)
        ball1.set_speed(0.5, 0)
        '''

        # Tests All:
        ball1.set_position(0, 0)
        ball1.set_speed(random(), random())

        block = Block(Vector(300, 200), Dimension(200, 200))
        block.select_bloc(BlockType.b1)

        self.windows.add_element(ball1, block)

        game_is_active = True
        while game_is_active:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    game_is_active = False

            self.windows.update()
            update(self.windows, ball1, block)
            if collision_check(ball1, block):
                ball1.speed.multiplication(0)
                print("Plataforma", block.position, block.dimension)
                print("Bola      ", ball1.position, ball1.dimension)
                print("area de colisão:", collider_bloc_ball(block, ball1))

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
