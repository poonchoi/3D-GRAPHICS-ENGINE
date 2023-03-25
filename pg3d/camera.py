import pg3d.MatrixMath.matrix as mm
from pg3d.matrices import *
import pygame as pg


class Camera:
    def __init__(self, app, position):
        self.app = app

        self.pos = mm.Matrix([[*position, 1]])
        self.forward = mm.Matrix([[0, 0, 1, 1]])
        self.up = mm.Matrix([[0, 1, 0, 1]])
        self.right = mm.Matrix([[1, 0, 0, 1]])

        self.speed = 1
        self.angle = m.radians(1)


    def yaw(self, angle):
        self.up *= rotate_y(angle)
        self.forward *= rotate_y(angle)
        self.right *= rotate_y(angle)


    def pitch(self, angle):
        self.up *= rotate_x(angle)
        self.forward *= rotate_x(angle)
        self.right *= rotate_x(angle)


    def rot_mat(self):
        fx, fy, fz, fw = self.forward[0]
        rx, ry, rz, rw = self.right[0]
        ux, uy, uz, uw = self.up[0]

        return mm.Matrix([[rx, ux, fx, 0],
                          [ry, uy, fy, 0],
                          [rz, uz, fz, 0],
                          [ 0,  0,  0, 1]])
    

    def trans_mat(self):
        x, y, z, w = self.pos[0]

        return mm.Matrix([[1, 0, 0, 0],
                          [0, 1, 0, 0],
                          [0, 0, 1, 0],
                          [-x,-y,-z,1]])
    

    def cam_mat(self):
        return self.trans_mat() * self.rot_mat()


    def movement(self):
        key = pg.key.get_pressed()

        if key[pg.K_a]:
            self.right = self.speed * self.right
            self.pos = self.pos - self.right
        if key[pg.K_d]:
            self.right = self.speed * self.right
            self.pos = self.pos + self.right
        if key[pg.K_w]:
            self.forward = self.speed * self.forward
            self.pos = self.pos + self.forward
        if key[pg.K_s]:
            self.forward = self.speed * self.forward
            self.pos = self.pos - self.forward
        if key[pg.K_q]:
            self.up = self.speed * self.up
            self.pos = self.pos + self.up
        if key[pg.K_e]:
            self.up = self.speed * self.up
            self.pos = self.pos - self.up

        if key[pg.K_LEFT]:
            self.yaw(-self.angle)
        if key[pg.K_RIGHT]:
            self.yaw(self.angle)
        if key[pg.K_UP]:
            self.pitch(self.angle)
        if key[pg.K_DOWN]:
            self.pitch(-self.angle)

        
        # x, y = pg.mouse.get_pos()
        # self.yaw((x - self.app.hwidth)/1000)
        # self.pitch((y - self.app.hheight)/1000)
        # pg.mouse.set_pos((self.app.hwidth, self.app.hheight))
        
