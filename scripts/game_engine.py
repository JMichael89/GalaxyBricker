import pygame

from scripts.characters.ball import Ball, BallType
from scripts.characters.block import Block, BlockType
from scripts.characters.platform import Platform, PlatformType
from scripts.utils.vector import Vector
from scripts.utils.window import Window


class GameEngine:
    def __init__(self):
        self.pygame = pygame
        self.pygame.init()
        self.windows = Window(pygame, "Galaxy Bricker", Vector(800, 600))

    def run(self):
        ball_was_thrown = False

        ball = self.generate_ball()

        blocks = self.generate_blocs(self.windows.dimension)

        platform = self.generate_platform(self.windows.dimension)
        self.windows.add_element(ball, *blocks, platform)

        game_is_active = True
        while game_is_active:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    game_is_active = False

            self.update_elements(self.windows, ball, blocks, platform)
            self.windows.update()

        pygame.quit()

    def update_elements(self, windows, ball, blocks, platform):
        keys = pygame.key.get_pressed()
        platform.direction.x = 0

        if keys[pygame.K_LEFT]:
            if platform.position.x >= 0:
                platform.direction.x = -1

        if keys[pygame.K_RIGHT]:
            if (platform.position.x + platform.dimension.x) <= windows.dimension.x:
                platform.direction.x = 1

        if keys[pygame.K_UP]:
            self.throw_ball(platform, ball)

        if (ball.position.x + ball.dimension.x) >= windows.dimension.x:
            ball.direction.x *= -1
        elif ball.position.x < 0:
            ball.direction.x *= -1

        if ball.position.y >= windows.dimension.y:
            ball.remove(ball)
            windows.remove_element(ball)
        elif ball.position.y < 0:
            ball.direction.y *= -1

    @staticmethod
    def throw_ball(platform: Platform, ball: Ball):
        ball.set_direction(platform.direction.x, 1)

    @staticmethod
    def generate_ball():
        raio = 20
        ball = Ball()
        ball.set_dimension(raio, raio)
        ball.select_character(BallType.basic_white)
        ball.speed_max = 0.5
        return ball

    @staticmethod
    def generate_blocs(window_size: Vector):
        blocks = []
        for y in range(10):
            for x in range(10):
                block = Block()
                block.set_dimension(-2 + window_size.x / 10, 18)
                block.select_character(BlockType.b1)
                block.set_position(2 + (x * (window_size.x - 2) / 10), y * 20 + 2)
                blocks.append(block)
        return blocks

    @staticmethod
    def generate_platform(window_size: Vector):
        platform = Platform()
        platform.set_dimension(120, 15)
        platform.select_character(PlatformType.animate1)
        platform.speed = 0.5

        platform.set_position(window_size.x / 2 - platform.get_width() / 2, window_size.y - 2 * platform.get_height())
        return platform
