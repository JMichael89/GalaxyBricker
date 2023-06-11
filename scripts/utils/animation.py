from typing import Optional

from PIL import Image

import pygame

from scripts.models.element import Element


class Animation(Element):
    def __init__(self, path_to_image, dimension=None):
        super().__init__(dimension)
        self.FORMAT = "RGBA"

        self.gif_img = Image.open(path_to_image)
        if not getattr(self.gif_img, "is_animated", False):
            raise Exception("The path does not lead to a gif file")

        self.nframe = 0
        self.current_frame = 0
        self._frame = self.pil_to_game(self.get_gif_frame(self.gif_img, self.current_frame))
        self.continuos = True

    def update_gif(self, path_to_image, dimension=None):
        self.__init__(path_to_image, dimension)

    @property
    def frame(self):
        if self.dimension is None:
            return self._frame
        return pygame.transform.scale(self._frame, (self.dimension.x, self.dimension.y))

    def update_frame(self):
        if self.continuos or self.nframe < self.gif_img.n_frames:
            self._frame = self.pil_to_game(self.get_gif_frame(self.gif_img, self.current_frame))
            self.current_frame = (self.current_frame + 1) % self.gif_img.n_frames
            self.nframe += 1
            return True
        else:
            return False

    def pil_to_game(self, img):
        data = img.tobytes("raw", self.FORMAT)
        return pygame.image.fromstring(data, img.size, self.FORMAT)

    def get_gif_frame(self, img, frame):
        img.seek(frame)
        return img.convert(self.FORMAT)

    @frame.setter
    def frame(self, value):
        self._frame = value

    def __str__(self):
        return "Animation"
