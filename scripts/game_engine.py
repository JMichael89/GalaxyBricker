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
        ball = self.generate_ball(self.windows.dimension)
        blocks = self.generate_blocs(self.windows.dimension)
        platform = self.generate_platform(self.windows.dimension)
        self.put_ball_in_platform(platform, ball)

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
            platform.move_to_left()
            self.put_ball_in_platform(platform, ball)

        if keys[pygame.K_RIGHT]:
            platform.move_to_right()
            self.put_ball_in_platform(platform, ball)

        if keys[pygame.K_UP]:
            self.throw_ball(platform, ball)

        for block in blocks:
            if block.check_hit(ball):
                blocks.remove(block)
                windows.remove_element(block)
                del block

    @staticmethod
    def throw_ball(platform: Platform, ball: Ball):
        if not ball.was_thrown:
            ball.set_direction(platform.direction.x * 0.25, -1)
            ball.speed = ball.speed_max
            ball.was_thrown = True

    @staticmethod
    def generate_ball(window_size):
        raio = 20
        ball = Ball()
        ball.set_dimension(raio, raio)
        ball.select_character(BallType.basic_white)
        ball.speed_max = 0.3
        ball.restrict_area_of_movement(0, window_size.x, 0, window_size.y)
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
        platform.restrict_area_of_movement(0, window_size.x, 0, window_size.y - 2 * platform.get_height())
        return platform

    @staticmethod
    def put_ball_in_platform(platform: Platform, ball: Ball):
        if not ball.was_thrown:
            position_x = platform.get_center().x - ball.get_radius()
            position_y = platform.position.y - ball.get_height()
            ball.set_position(position_x, position_y)
