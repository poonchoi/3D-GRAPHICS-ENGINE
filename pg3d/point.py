import pygame as pg
import pg3d.MatrixMath.matrix as mm
import math as m
from pygame.colordict import THECOLORS


class Point:
    def __init__(self, app, coordinate, vertex=True):
        """
        Creates the point

        Args:
            app ([App]): [instance of App class]
            coordinate ([list]): [coordinate of point]
            vertex (bool, optional): [flag that says whether point is drawn]. Defaults to True.
        """
        self.coordinate = mm.Matrix([[*coordinate, 1]])
        self.app = app
        self.app.add_point(self)
        self.vertex = vertex

    def __repr__(self):
        """
        Defines the behaviour of printing Point objects

        Returns:
            [str]: [String representation of point]
        """
        return str(self.coordinate[0])

    def __setitem__(self, index, value):
        """
        Defines the behaviour of setting an indexed Point object to a value

        Args:
            index ([int]): [position of point]
            value ([float]): [vew value of coordinate]
        """
        self.coordinate[0][index] = value

    def __getitem__(self, index):
        """
        Defines the behaviour for indexing a Point object

        Args:
            index ([int]): [position of coordinate]

        Returns:
            [float]: [coordinate that was indexed]
        """
        if index == 0 or index == 1 or index == 2 or index == 3:
            return self.coordinate[0][index]

        else:
            return "invalid position"

    def project(self, proj, cam):
        """
        projects point

        Args:
            proj ([Matrix]): [projection matrix]
            cam ([Matrix]): [camera matrix]

        Returns:
            [tuple]: [Returns projected point]
        """
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
