import sys

import pygame

from scripts.characters.ball import Ball, BallType
from scripts.characters.block import Block, BlockType
from scripts.characters.platform import Platform, PlatformType
from scripts.utils.window import Window


class GamePlay:

    def __init__(self, window, clock, level):
        self.ball = None
        self.blocks = []
        self.platform = None
        self.level = level
        self.clock = clock
        self.window = window

    def init(self):
        self.ball = self.generate_ball()
        self.platform = self.generate_platform(self.window.width, self.window.height)
        self.blocks = []
        self.blocks = self.generate_blocks()
        self.window.add_element(self.ball, self.platform, *self.blocks)

        self.put_ball_in_platform()

        game_is_active = True
        while game_is_active:
            if self._listen_keyboard():
                return

            self.update_elements()
            self.window.update()

        pygame.quit()

    def _listen_keyboard(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.key == pygame.K_ESCAPE:
                return True
            elif event.key == pygame.K_LEFT:
                self.platform.move_to_left(self.window.width)
                self.put_ball_in_platform()

            elif event.key == pygame.K_RIGHT:
                self.platform.move_to_right(self.window.width)
                self.put_ball_in_platform()

            elif event.key == pygame.K_UP:
                self.throw_ball()

            elif event.key == pygame.K_DOWN:
                self.ball.was_thrown = False
                self.ball.direction.multiplication_by(0)
                self.put_ball_in_platform()
    def update_elements(self):
        keys = pygame.key.get_pressed()
        self.platform.direction.x = 0

        if keys[pygame.K_ESCAPE]:
            return True

        if keys[pygame.K_LEFT]:
            self.platform.move_to_left(self.window.width)
            self.put_ball_in_platform()

        if keys[pygame.K_RIGHT]:
            self.platform.move_to_right(self.window.width)
            self.put_ball_in_platform()

        if keys[pygame.K_UP]:
            self.throw_ball()

        if keys[pygame.K_DOWN]:
            self.ball.was_thrown = False
            self.ball.direction.multiplication_by(0)
            self.put_ball_in_platform()

        for block in self.blocks:
            if self.ball.check_collide(block):
                self.ball.calculate_result_direction(block)
                if block.check_hit():
                    self.blocks.remove(block)
                    self.window.remove_element(block)
                    del block

        if self.ball.check_collide(self.platform):
            self.ball.direction.y *= -1
            self.ball.direction.x += self.platform.direction.x * 0.25

        self.ball.check_collider_by_window(self.window)

        if self.ball.check_die(self.window):
            self.window.remove_element(self.ball)
            self.ball = self.generate_ball()
            self.window.add_element(self.ball)
            self.put_ball_in_platform()

    def throw_ball(self):
        if not self.ball.was_thrown:
            self.ball.set_direction(self.platform.direction.x * 0.5, -1)
            self.ball.was_thrown = True

    @staticmethod
    def generate_platform(window_width, window_height):
        platform = Platform()
        platform.set_dimension(120, 15)
        platform.select_character(PlatformType.animate1)
        platform.speed = 1

        platform.set_position(window_width / 2 - platform.get_width() / 2, window_height - 2 * platform.get_height())
        return platform

    @staticmethod
    def generate_ball():
        raio = 20
        ball = Ball()
        ball.set_dimension(raio, raio)
        ball.select_character(BallType.basic_white)
        ball.speed = 1
        return ball

    def generate_blocks(self):
        print("generate_blocks")
        block_width = self.window.width / 10
        block_height = 20
        blocks = []
        for i in range(len(self.level)):
            for j in range(len(self.level[i])):
                if self.level[i][j] == 1:
                    block_x = j * block_width
                    block_y = i * block_height * 1.1
                    block = self.generate_block(block_x, block_y, block_width, block_height)
                    blocks.append(block)
        return blocks

    @staticmethod
    def generate_block(x, y, width, height):
        block = Block()
        block.set_position(x, y)
        block.set_dimension(width, height)
        block.select_character(BlockType.b1)

        return block

    def put_ball_in_platform(self):
        if not self.ball.was_thrown:
            position_x = self.platform.get_center().x - self.ball.get_radius()
            position_y = self.platform.position.y - self.ball.get_height()
            self.ball.set_position(position_x, position_y)
