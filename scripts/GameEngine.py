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
        self.windows = Window(pygame, "Galaxy Bricker", Dimension(800, 600))

    def run(self):

        balls = []
        for x in range(1):
            balls.append(generate_ball())

        blocks = []
        blocks = generate_bloc(self.windows.dimension)

        platform = generate_platform(self.windows.dimension, balls[0])
        self.windows.add_element(*balls, *blocks, platform)

        game_is_active = True
        while game_is_active:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    game_is_active = False

            update_elements(self.windows, balls, blocks, platform)
            self.windows.update()

        pygame.quit()


def update_elements(windows, balls, blocks, platform):
    keys = pygame.key.get_pressed()
    platform.direction.x = 0

    if keys[pygame.K_LEFT]:
        if platform.position.x >= 0:
            platform.direction.x = -1

    if keys[pygame.K_RIGHT]:
        if (platform.position.x + platform.dimension.x) <= windows.dimension.x:
            platform.direction.x = 1

    if keys[pygame.K_UP]:
        platform.throw_ball()

    for block in [*blocks]:
        for ball in [*balls]:
            if check_collision(block, ball) is True:
                if check_external_collider(block, ball):
                    blocks.remove(block)
                    windows.remove_element(block)
                    break

    for ball in [*balls]:
        if check_collision(platform, ball) is True:
            if check_external_collider(platform, ball):
                break

    for ball in balls:
        if (ball.position.x + ball.dimension.x) >= windows.dimension.x:
            ball.direction.x *= -1
        elif ball.position.x < 0:
            ball.direction.x *= -1

        if ball.position.y >= windows.dimension.y:
            balls.remove(ball)
            windows.remove_element(ball)
        elif ball.position.y < 0:
            ball.direction.y *= -1

    if balls.__len__() == 0:
        ball = generate_ball()
        platform.update_ball(ball)
        balls.append(ball)
        windows.add_element(ball)


def generate_ball():
    raio = 20
    ball = Ball(dimension=Dimension(raio, raio))
    ball.select_ball(BallType.basic_white)
    ball.speed_max = 0.5
    return ball


def generate_bloc(window_size: Vector):
    blocks = []
    for y in range(10):
        for x in range(10):
            block = Block(dimension=Dimension(-2 + window_size.x / 10, 18))
            block.select_bloc(BlockType.b1)
            block.set_position(2 + (x * (window_size.x - 2) / 10), y * 20 + 2)
            blocks.append(block)
    return blocks


def generate_platform(window_size: Vector, ball):
    platform = Platform(dimension=Dimension(120, 15), ball=ball)
    platform.select_platform(PlatformType.animate1)
    platform.set_speed(0.5)

    platform.set_position(window_size.x / 2 - platform.get_width() / 2, window_size.y - 2 * platform.get_height())
    return platform
