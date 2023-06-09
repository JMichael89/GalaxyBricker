import sys

import pygame

from scripts.characters.ball import Ball, BallType
from scripts.characters.block import Block, BlockType
from scripts.characters.platform import Platform, PlatformType
from scripts.models.text_view import TextView


class GamePlay:

    def __init__(self, window, clock, level):
        self.life = 3
        self.ball = None
        self.blocks = []
        self.platform = None
        self.level = level
        self.clock = clock
        self.window = window

        self.win = TextView("Win", "Arial", int(self.window.width * 0.075), (0, 255, 0))
        self.win.set_position(int(self.window.width * 0.45), int(self.window.height * 0.8))

        self.lose = TextView("Lose", "Arial", int(self.window.width * 0.075), (0, 255, 0))
        self.lose.set_position(int(self.window.width * 0.45), int(self.window.height * 0.8))

    def init(self):
        self.ball = self.generate_ball(self.window.width, self.window.height)
        self.platform = self.generate_platform(self.window.width, self.window.height)
        self.blocks = []
        self.blocks = self.generate_blocks()
        self.window.add_element(self.ball, self.platform, *self.blocks)

        self.put_ball_in_platform()

        game_is_active = True
        while game_is_active:
            if self._listen_keyboard():
                return
            if len(self.blocks) == 0:
                # Ganhou
                self.ball.speed = 0
                self.platform.speed = 0
                self.window.add_element(self.win)
                return
            if self.life == 0:
                # Perdeu
                self.ball.speed = 0
                self.platform.speed = 0
                self.window.add_element(self.lose)
                return

            self.clock.tick(int(600 * self.window.width/1000))
            print(self.clock.get_fps())
            self.update_elements()
            self.window.update()

        pygame.quit()

    def _listen_keyboard(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        self.platform.direction.x = 0
        keys = pygame.key.get_pressed()
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

        elif keys[pygame.K_ESCAPE]:
            return True

    def update_elements(self):
        for block in self.blocks:
            if self.ball.check_collide(block):
                if block.hit(self.ball.power):
                    self.blocks.remove(block)
                    self.window.remove_element(block)
                    del block

        if self.ball.check_collide(self.platform):
            self.ball.direction.x += self.platform.direction.x * 0.25 * self.platform.speed
            aux = -(((self.platform.position.x - self.ball.get_center().x) / self.platform.get_width()) + 0.5)
            self.ball.direction.x = aux
            self.ball.direction.y = -1
            self.ball.position.y -= 5

        self.ball.check_collider_by_window(self.window)

        if self.ball.check_die(self.window):
            self.window.remove_element(self.ball)
            self.ball = self.generate_ball(self.window.width, self.window.height)
            self.window.add_element(self.ball)
            self.put_ball_in_platform()
            self.life -= 1

    def throw_ball(self):
        if not self.ball.was_thrown:
            self.ball.set_direction(self.platform.direction.x * 0.5, -1)
            self.ball.was_thrown = True

    @staticmethod
    def generate_platform(window_width, window_height):
        platform = Platform()
        platform.set_dimension(window_width * 0.2, window_height * 0.025)
        platform.select_character(PlatformType.animate1)
        platform.speed = 1.5

        platform.set_position(window_width / 2 - platform.get_width() / 2, window_height * 0.9)
        return platform

    @staticmethod
    def generate_ball(window_width, window_height):
        raio = window_height * 0.025
        ball = Ball()
        ball.set_dimension(raio, raio)
        ball.select_character(BallType.basic_white)
        ball.speed = 1.5
        return ball

    def generate_blocks(self):
        block_width = self.window.width / len(self.level[0])
        block_height = self.window.height * 0.04
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
        block.life = 4

        return block

    def put_ball_in_platform(self):
        if not self.ball.was_thrown:
            position_x = self.platform.get_center().x - self.ball.get_radius()
            position_y = self.platform.position.y - self.ball.get_height()
            self.ball.set_position(position_x, position_y)
