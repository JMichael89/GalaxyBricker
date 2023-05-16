from random import random, randrange

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
        ball1.set_position(0, 0)
        ball1.set_speed(random(), random())

        ball2 = Ball(dimension=Dimension(20, 20))
        ball2.select_ball(BallType.basic_white)
        ball2.set_position(0, 579)
        ball2.set_speed(random(), random())

        ball3 = Ball(dimension=Dimension(20, 20))
        ball3.select_ball(BallType.basic_white)
        ball3.set_position(759, 0)
        ball3.set_speed(random(), random())

        ball4 = Ball(dimension=Dimension(20, 20))
        ball4.select_ball(BallType.basic_white)
        ball4.set_position(759, 579)
        ball4.set_speed(random(), random())

        block1 = Block(Vector(randrange(0, 700), randrange(0, 520)), Dimension(randrange(20, 100), randrange(20, 100)))
        block1.select_bloc(BlockType.b1)

        block2 = Block(Vector(randrange(0, 700), randrange(0, 520)), Dimension(randrange(20, 100), randrange(20, 100)))
        block2.select_bloc(BlockType.b1)

        block3 = Block(Vector(randrange(0, 700), randrange(0, 520)), Dimension(randrange(20, 100), randrange(20, 100)))
        block3.select_bloc(BlockType.b1)

        block4 = Block(Vector(randrange(0, 700), randrange(0, 520)), Dimension(randrange(20, 100), randrange(20, 100)))
        block4.select_bloc(BlockType.b1)

        block5 = Block(Vector(randrange(0, 700), randrange(0, 520)), Dimension(randrange(20, 100), randrange(20, 100)))
        block5.select_bloc(BlockType.b1)

        block6 = Block(Vector(randrange(0, 700), randrange(0, 520)), Dimension(randrange(20, 100), randrange(20, 100)))
        block6.select_bloc(BlockType.b1)

        block7 = Block(Vector(randrange(0, 700), randrange(0, 520)), Dimension(randrange(20, 100), randrange(20, 100)))
        block7.select_bloc(BlockType.b1)

        block8 = Block(Vector(randrange(0, 700), randrange(0, 520)), Dimension(randrange(20, 100), randrange(20, 100)))
        block8.select_bloc(BlockType.b1)



        self.windows.add_element(ball1, ball2, ball3, ball4, block1, block2, block3, block4, block5, block6, block7, block8)

        game_is_active = True
        while game_is_active:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    game_is_active = False

            self.windows.update()
            update(self.windows, ball1, ball2, ball3, ball4, block1, block2, block3, block4, block5, block6, block7, block8)

            for block in [block1, block2, block3, block4, block5, block6, block7, block8]:
                for ball in [ball1, ball2, ball3, ball4]:
                    if collision_check(ball, block):
                        print("area de colisão:", collider_bloc_ball(block, ball))

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
