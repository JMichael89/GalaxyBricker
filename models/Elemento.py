from abc import ABC
from tkinter import PhotoImage

from models.utils import Vector, Dimension


class Elemento(ABC):
    def __init__(self, positions: Vector, dimensions: Dimension, image: PhotoImage):
        self.positions = positions
        self.dimensions = dimensions
        self.image = image


