import numpy as np
import pygame as pg
from pg3dmarch.matrices import *

class Camera():
    def __init__(self, app):
        self.app = app

        self.position = np.matrix([[0, 0, 0, 1]])

        self.forward = np.matrix([[0, 0, 1, 1]])
        self.up = np.matrix([[0, 1, 0, 1]])
        self.right = np.matrix([[1, 0, 0, 1]])

        self.h_fov = 60
        self.aspect_ratio = app.res[1] / app.res[0]
        self.v_fov = self.h_fov * self.aspect_ratio
        self.near = 0.1
        self.far = 1000

        self.movement_speed = 0.3
        self.rotation_speed = m.radians(0.1)


    def camera_translate(self):
        x, y, z, w = self.position[0]
        return np.matrix([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [-x,-y,-z,1]])


    def rotation_matrix(self):
        fx, fy, fz, fw = self.forward[0]
        ux, uy, uz, uw = self.up[0]
        rx, ry, rz, rw = self.right[0]
        return np.matrix([
            [rx,ux,fx,0],
            [ry,uy,fy,0],
            [rz,uz,fz,0],
            [0, 0, 0, 1]])
    

    def camera_matrix(self):
        return self.camera_translate() @ self.rotation_matrix()
    

    def check_movement(self):
        """
        Checks for keyboard input and updates the position of the camera based on the key pressed
        """
        print(self.position)
        key = pg.key.get_pressed()

        if key[pg.K_w]:
            self.position += (self.movement_speed * self.forward)

        if key[pg.K_s]:
            self.position -= (self.movement_speed * self.forward)

        if key[pg.K_a]:
            self.position += (self.movement_speed * self.right) * 5

        if key[pg.K_d]:
            self.position -= (self.movement_speed * self.right) * 5
        
        if key[pg.K_LEFT]:
            self.yaw(-self.rotation_speed)

        if key[pg.K_RIGHT]:
            self.yaw(self.rotation_speed)

        if key[pg.K_UP]:
            self.pitch(-self.rotation_speed)

        if key[pg.K_DOWN]:
            self.pitch(self.rotation_speed)


    def pitch(self, angle):
        self.forward *= rotate_x(angle)
        self.right *= rotate_x(angle)
        self.up *= rotate_x(angle)


    def yaw(self, angle):
        self.forward *= rotate_y(angle)
        self.right *= rotate_y(angle)
        self.up *= rotate_y(angle)
