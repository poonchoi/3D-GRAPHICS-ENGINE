import pygame as pg
import numpy as np

class cube:
    def __init__(self, size, coordinates):
        self.size = size
        self.coordinates = coordinates
        self.points = points = [[-1, -1, 1], [1, -1, 1], [1, 1, 1], [-1, 1, 1], [-1, -1, -1], [1, -1, -1], [1, 1, -1], [-1, 1, -1]]
    