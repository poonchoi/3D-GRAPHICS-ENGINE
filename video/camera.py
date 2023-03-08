from matrices import *
import math as m
import numpy as np

class Camera:
    def __init__(self, app, pos):
        self.app = app
        self.pos = pos
        self.forward = np.array([0,1,1,1])
        self.right = np.array([1,0,0,1])
        self.up = np.array([0,1,0,1])
        self.hfov = m.pi / 3
        self.vfov = self.hfov * (app.height / app.width)
        self.near = 0.1
        self.far = 100

    def translate_matrix(self):
        x, y, z, w = self.pos
        return np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [-x, -y, -z, 1]])

    def rotate_matrix(self):
        rx, ry, rz, w = self.right
        fx, fy, fz, w = self.forward
        ux, uy, uz, w = self.up
        return np.array([
            [rx, ux, fx, 0],
            [ry, uy, fy, 0],
            [rz, uz, fz, 0],
            [0, 0, 0, 1]])
    
    def camera_matrix(self):
        return self.translate_matrix() @ self.rotate_matrix()