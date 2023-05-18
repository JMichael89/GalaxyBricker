from random import random, randrange

from scripts.characters.Ball import Ball, BallType
from scripts.characters.Block import Block, BlockType
from scripts.characters.Platform import Platform, PlatformType
from scripts.models.Collider import check_collision, check_external_collider
from scripts.utils.Vector import Vector
from scripts.utils.Window import Window
from scripts.utils.Dimension import Dimension

import pygame


class GameEngine:
    def __init__(self):
        self.pygame = pygame
        self.pygame.init()
        self.windows = Window(pygame, "Galaxy Bricker", Dimension(400, 400))

    def run(self):

        tests = "true"
        ball_test = Ball(dimension=Dimension(20, 20))
        ball_test.select_ball(BallType.basic_white)
        block_test = Block()
        block_test.select_bloc(BlockType.b1)

        # Tests A2
        ball_test.set_position(0, 0)
        ball_test.set_speed(random(), random())

        block_test = Block(Vector(100, 100), Dimension(200, 200))
        block_test.select_bloc(BlockType.b1)

        self.windows.add_element(ball_test, block_test)

        game_is_active = True
        while game_is_active:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    game_is_active = False

            self.windows.update()

            if tests == "true":
                for block in [block_test]:
                    for ball in [ball_test]:
                        if check_collision(block, ball):
                            if check_external_collider(block, ball):
                                #tests = "break"
                                #ball.speed.multiplication(0)
                                #print("ball  :", ball.position)
                                #print("block :", block.position)
                                ...

            update(self.windows, ball_test, block_test)

        pygame.quit()


def update(windows, *elements):
    for element in elements:
        if (element.position.x + element.dimension.x) >= windows.dimension.x:
            element.speed.x *= -1
        elif element.position.x < 0:
            element.speed.x *= -1

        if (element.position.y + element.dimension.y) >= windows.dimension.y:
            element.speed.y *= -1
        elif element.position.y < 0:
            element.speed.y *= -1
