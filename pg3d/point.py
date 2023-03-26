import pygame as pg
import pg3d.MatrixMath.matrix as mm
import math as m
from pygame.colordict import THECOLORS


class Point:
    def __init__(self, app, coordinate, vertex=True):
        self.coordinate = mm.Matrix([[*coordinate, 1]])
        self.app = app
        self.app._add_point(self)
        self.vertex = vertex

    def __repr__(self):
        """
        Defines the behaviour of printing Point objects
        """
        return str(self.coordinate[0])

    def __setitem__(self, index, value):
        """
        Defines the behaviour of setting an indexed Point object to a value
        """
        self.coordinate[0][index] = value

    def __getitem__(self, index):
        """
        Defines the behaviour for indexing a Point object
        """
        if index == 0 or index == 1 or index == 2 or index == 3:
            return self.coordinate[0][index]

        else:
            return "invalid position"

    def _project(self, proj, cam):
        copy = mm.copy_matrix(self.coordinate)
        copy *= cam
        projected = copy * proj
        x, y, z, w = projected[0]

        if w != 0:
            x /= w
            y /= w
            z /= w
            if (x < 2 and x > -2) and (y < 2 and y > -2):
                x, y = (x + 1) * self.app.half_width, (y + 1) * self.app.half_height
                return (x, y, z)
            else:
                return None
