import numpy as np
from matrices import *
import pygame as pg


class Object:
    def __init__(self, app):
        self.app = app
        self.vertices = np.array([[0,0,0,1], [0,1,0,1], [0,1,1,1], [1,1,1,1], [1,1,0,1], [1,0,1,1], [1,0,0,1], [0,0,1,1]])

    def draw(self):
        self.screen_projection()

    def screen_projection(self):
        vertices = self.vertices @ self.app.camera.camera_matrix()
        vertices = vertices @ self.app.projection.projection_matrix
        vertices /= vertices[:,-1].reshape(-1,1)
        vertices[(vertices > 1) | (vertices < -1)] = 0
        vertices = vertices @ self.app.projection.to_screen_matrix
        vertices = vertices[:,:,2]

        for vertex in vertices:
            if not np.any((vertex == self.app.h_width) | (vertex == self.app.h_height)):
                pg.draw.circle(self.app.screen, pg.Color('white'), vertex, 7)

    def translate(self, pos):
        self.vertices = self.vertices @ translate(pos)

    def scale(self, scale):
        self.vertices = self.vertices @ scale(scale)

    def rotate_x(self, a):
        self.vertices = self.vertices @ rotate_x(a)

    def rotate_y(self, a):
        self.vertices = self.vertices @ rotate_y(a)

    def rotate_z(self, a):
        self.vertices = self.vertices @ rotate_z(a)