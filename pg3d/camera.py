import pygame as pg
import math as m
import pg3d.MatrixMath.matrix as mm
from pg3d.matrices import *


class Camera():
    def __init__(self, position):
        self.position = mm.Matrix([position])
        self.orientation = [0, 0]

        # direction that the camera is looking at
        self.forward = mm.Matrix([[1, 0, 1, 1]])
        self.up = mm.Matrix([[0, 1, 0, 1]])
        self.right = mm.Matrix([[1, 0, 0, 1]])

        self.movement_speed = 1
        self.rotation_speed = 0.001
        self.pitch_a = 0
        self.yaw_a = 0


    def check_movement(self):
        """
        Checks for keyboard input and updates the position of the camera based on the key pressed
        """
        key = pg.key.get_pressed()

        if key[pg.K_w]:
            self.position += (self.movement_speed * self.forward)
        if key[pg.K_s]:
            self.position = self.position - (self.movement_speed * self.forward)
        if key[pg.K_a]:
            self.position = self.position - (self.movement_speed * self.right)
        if key[pg.K_d]:
            self.position = self.position + (self.movement_speed * self.right)
        
        if key[pg.K_RIGHT]:
            self.yaw_a += self.rotation_speed
            self.yaw(self.yaw_a)
        if key[pg.K_LEFT]:
            self.yaw_a -= self.rotation_speed
            self.yaw(self.yaw_a)
        if key[pg.K_UP]:
            self.pitch_a += self.rotation_speed
            self.pitch(self.pitch_a)
        if key[pg.K_DOWN]:
            self.pitch_a += self.rotation_speed
            self.pitch(self.pitch_a)


    def pitch(self, angle):
        """
        Rotates the camera along the x-axis
        The axes get multipied by the rotation matrix
        """
        rot = rotate_x(angle)
        self.up = self.up * rot
        self.right = self.right * rot
        self.forward = self.forward * rot
    

    def yaw(self, angle):
        """
        Rotates the camera along the y-axis
        The axes get multipied by the rotation matrix
        """
        rot = rotate_y(angle)
        self.up = self.up * rot
        self.right = self.right * rot
        self.forward = self.forward * rot


    def translate_matrix(self):
        """
        Returns a matrix which translates the point so that the camera is placed at the centre of the screen
        """
        x, y, z, w = self.position[0]
        return mm.Matrix([[1, 0, 0, 0],
                          [0, 1, 0, 0],
                          [0, 0, 1, 0],
                          [-x, -y, -z, 1]])


    def rotate_matrix(self):
        """
        Returns a matrix that rotates the points around the camrea 
        """
        rx, ry, rz, w = self.right[0]
        fx, fy, fz, w = self.forward[0]
        ux, uy, uz, w = self.up[0]
        return mm.Matrix([[rx, ux, fx, 0],
                          [ry, uy, fy, 0],
                          [rz, uz, fz, 0],
                          [0, 0, 0, 1]])


    def view_matrix(self):
        """
        Returns the dot product of the translate and rotate matrices
        """
        return self.translate_matrix() * self.rotate_matrix()