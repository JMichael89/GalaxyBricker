from random import randint

import pygame

from scripts.characters.ball import Ball, BallType
from scripts.characters.block import Block, BlockType
from scripts.characters.platform import Platform, PlatformType
from scripts.utils.vector import Vector
from scripts.utils.window import Window


def generate_randon_block():
    block = Block()
    block.set_dimension(randint(10, 200), randint(10, 200))
    block.select_character(BlockType.b1)
    block.set_position(randint(0, 700), randint(0, 400))
    return block


class GameEngine:
    def __init__(self):
        self.pygame = pygame
        self.pygame.init()
        self.windows = Window(pygame, "Galaxy Bricker", Vector(800, 600))

        self.ball = None
        self.blocks = []
        self.platform = None

    def run(self):
        self.ball = self.generate_ball()
        self.blocks = self.generate_blocs(self.windows.dimension)
        self.platform = self.generate_platform(self.windows.dimension)
        self.put_ball_in_platform()

        self.windows.add_element(self.ball, *self.blocks, self.platform)

        game_is_active = True
        while game_is_active:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    game_is_active = False

            self.update_elements(self.windows, self.ball, self.blocks, self.platform)
            self.windows.update()

        pygame.quit()

    def update_elements(self, windows, ball, blocks, platform):
        keys = pygame.key.get_pressed()
        platform.direction.x = 0

        if keys[pygame.K_LEFT]:
            platform.move_to_left(windows.dimension)
            self.put_ball_in_platform()

        if keys[pygame.K_RIGHT]:
            platform.move_to_right(windows.dimension)
            self.put_ball_in_platform()

        if keys[pygame.K_UP]:
            self.throw_ball(platform, ball)

        if keys[pygame.K_DOWN]:
            ball.was_thrown = False
            ball.direction.multiplication_by(0)
            self.put_ball_in_platform()

        if keys[pygame.K_SPACE]:
            ...

        for block in blocks:
            if ball.check_collide(block):
                ball.calculate_result_direction(ball, block)
                if block.check_hit():
                    #blocks.remove(block)
                    #windows.remove_element(block)
                    #del block
                    ...

        if ball.check_collide(platform):
            ball.calculate_result_direction(ball, platform)
            ball.direction.x += platform.direction.x * 0.1

        ball.check_collider_by_window(windows)

        if ball.check_die(windows):
            ball.direction.y *= -1
            #windows.remove_element(ball)
            #self.ball = self.generate_ball()
            #windows.add_element(self.ball)
            #self.put_ball_in_platform()

    @staticmethod
    def throw_ball(platform: Platform, ball: Ball):
        if not ball.was_thrown:
            ball.set_direction(platform.direction.x * 0.5, -1)
            ball.was_thrown = True

    @staticmethod
    def generate_ball():
        raio = 50
        ball = Ball()
        ball.set_dimension(raio, raio)
        ball.select_character(BallType.basic_white)
        ball.speed = 0.5
        return ball

    @staticmethod
    def generate_blocs(window_size: Vector):
        blocks = []
        for y in range(0):
            for x in range(0):
                block = Block()
                block.set_dimension(-2 + window_size.x / 10, 50)
                block.select_character(BlockType.b1)
                block.set_position(2 + (x * (window_size.x - 2) / 10), y * 20 + 2)
                blocks.append(block)

        block = Block()
        block.set_dimension(100, 100)
        block.select_character(BlockType.b1)
        block.set_position(350, 200)
        blocks.append(block)
        return blocks

    @staticmethod
    def generate_platform(window_size: Vector):
        platform = Platform()
        platform.set_dimension(120, 15)
        platform.select_character(PlatformType.animate1)
        platform.speed = 0.75

        platform.set_position(window_size.x / 2 - platform.get_width() / 2, window_size.y - 2 * platform.get_height())
        return platform

    def put_ball_in_platform(self):
        if not self.ball.was_thrown:
            position_x = self.platform.get_center().x - self.ball.get_radius()
            position_y = self.platform.position.y - self.ball.get_height()
            self.ball.set_position(position_x, position_y)
