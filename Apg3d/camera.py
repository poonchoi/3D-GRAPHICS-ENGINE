import Apg3d.MatrixMath.matrix as mm
from Apg3d.matrices import rotate_x, rotate_y, rotate_z
import pygame as pg
import math as m


class Camera:
    def __init__(self, position, forward=[0, 0, 1], up=[0, 1, 0], right=[1, 0, 0]):
        """
        Args:
            position ([list]): [Starting position of camera]
            forward ([list], optional): [Orientation along z-axis]. Defaults to [0, 0, 1].
            up ([list], optional): [Orientation along y-axis]. Defaults to [0, 1, 0].
            right ([list], optional): [Orientation along x-axis]. Defaults to [1, 0, 0].
        """
        self.pos = mm.Matrix([[*position, 1]])
        self._forward = mm.Matrix([[*forward, 1]])
        self._up = mm.Matrix([[*up, 1]])
        self._right = mm.Matrix([[*right, 1]])

        self.speed = 1
        self.angle = m.radians(1)

    def yaw(self, angle):
        """
        Rotates camera directions along y-axis by angle

        Args:
            angle ([float]): [Angle used to rotate camera orientation]
        """
        self._up *= rotate_y(angle)
        self._forward *= rotate_y(angle)
        self._right *= rotate_y(angle)

    def pitch(self, angle):
        """
        Rotates camera directions along x-axis by angle

        Args:
            angle ([float]): [Angle used to rotate camera orientation]
        """
        self._up *= rotate_x(angle)
        self._forward *= rotate_x(angle)
        self._right *= rotate_x(angle)

    def _rot_mat(self):
        """
        Creates rotation matrix

        Returns:
            [Matrix]: [Rotation matrix used to rotate all point in world space around camera]
        """
        fx, fy, fz, fw = self._forward[0]
        rx, ry, rz, rw = self._right[0]
        ux, uy, uz, uw = self._up[0]

        return mm.Matrix(
            [[rx, ux, fx, 0], [ry, uy, fy, 0], [rz, uz, fz, 0], [0, 0, 0, 1]]
        )

    def _trans_mat(self):
        """
        Creates translate matrix

        Returns:
            [Matrix]: [Translation matrix used to put camera at center of 3D space]
        """
        x, y, z, w = self.pos[0]

        return mm.Matrix([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [-x, -y, -z, 1]])

    def _cam_mat(self):
        """
        Creates camera matrix

        Returns:
            [Matrix]: [Camera matrix which is multiplied to all points]
        """
        return self._trans_mat() * self._rot_mat()

    def _movement(self):
        """
        Checks for user input and then performs the necessary rotations and translations
        """
        key = pg.key.get_pressed()

        if key[pg.K_a]:
            self._right = self.speed * self._right
            self.pos = self.pos - self._right
        if key[pg.K_d]:
            self._right = self.speed * self._right
            self.pos = self.pos + self._right
        if key[pg.K_w]:
            self._forward = self.speed * self._forward
            self.pos = self.pos + self._forward
        if key[pg.K_s]:
            self._forward = self.speed * self._forward
            self.pos = self.pos - self._forward
        if key[pg.K_q]:
            self._up = self.speed * self._up
            self.pos = self.pos + self._up
        if key[pg.K_e]:
            self._up = self.speed * self._up
            self.pos = self.pos - self._up

        if key[pg.K_LEFT]:
            self.yaw(-self.angle)
        if key[pg.K_RIGHT]:
            self.yaw(self.angle)
        if key[pg.K_UP]:
            self.pitch(self.angle)
        if key[pg.K_DOWN]:
            self.pitch(-self.angle)

    def _mouse_look(self, rel):
        """
        Moves camera when mouse is moved

        Args:
            rel ([float]): [relative position of mouse]
        """
        x, y = rel
        self.yaw(x / 1000)
        self.pitch(y / 1000)
