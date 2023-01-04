import pygame as pg
import math as m
import pg3d.MatrixMath.matrix as mm
from pg3d.camera import Camera
from pg3d.triangle import Triangle
from pg3d.point import Point


class World():
    def __init__(self, app):
        self.app = app
        self.camera = Camera([0, 0, 0, 1])
        self.z_speed = 0.07
        self.x_speed = 3
        self.angle = .01

        self.dimensions = self.app.RES
        self.width = self.dimensions[0]
        self.height = self.dimensions[1]
        self.h_width = self.width // 2
        self.h_height = self.height // 2
        self.screen = self.app.screen

        self.mesh = []

        self.n = 0.1
        self.f = 10
        self.a = self.width / self.height
        self.h_fov = m.radians(90)
        self.v_fov = self.h_fov * self.a


    def add_point(self, point):
        """
        Appends a singular point to the mesh list
        """
        self.mesh.append([point])


    def add_triangle(self, triangle):
        """
        Appends a triangle to the mesh list
        """
        self.mesh.append(triangle)


    def translate(self, new_pos):
        """
        Moves point by given values in x, y & z
        """
        x, y, z = new_pos
        for polygon in self.mesh:
            for point in polygon:
                point[0] += x
                point[1] += y
                point[2] += z


    # def projection_matrix(self):
    #     n = self.n
    #     f = self.f
    #     fov = self.fov
    #     a = self.a

    #     fov_rad = m.radians(fov)
    #     t = m.tan(fov_rad / 2) * n
    #     b = -t
    #     r = t * a
    #     l = -r

    #     return mm.Matrix([[(2*n)/(r-l), 0, (r+l)/(r-l), 0],
    #                       [0, (2*n)/(t-b), (t+b)/(t-b), 0],
    #                       [0, 0, -(f+n)/(f-n), -(2*f*n)/(f-n)],
    #                       [0, 0, 1, 0]])
    def projection_matrix(self):
        """
        Creates the projection matrix to project the points onto the screen
        """
        n = self.n
        f = self.f
        h_fov = self.h_fov
        v_fov = self.v_fov
        a = self.a

        t = m.tan(v_fov / 2)
        b = -t
        r = m.tan(h_fov / 2)
        l = -r

        m00 = 2 / (r - l)
        m11 = 2 / (t - b)
        m22 = (f + n) / (f - n)
        m32 = -(2 * f * n) / (f - n)

        return mm.Matrix([[m00, 0, 0, 0],
                          [0, m11, 0, 0],
                          [0, 0, m22, 0],
                          [0, 0, m32, 0]])


    # def view_matrix(self):
    #     pitch, yaw = m.radians(self.camera.orientation[0]), m.radians(self.camera.orientation[1])

    #     y_rot = mm.Matrix([[m.cos(yaw), 0, m.sin(yaw)],
    #                        [0, 1, 0],
    #                        [-m.sin(yaw), 0, m.cos(yaw)]])

    #     x_rot = mm.Matrix([[1, 0, 0],
    #                        [0, m.cos(pitch), -m.sin(pitch)],
    #                        [0, m.sin(pitch), m.cos(pitch)]])

    #     o = x_rot * y_rot

    #     R00, R01, R02 = o[0][0], o[0][1], o[0][2]
    #     R10, R11, R12 = o[1][0], o[1][1], o[1][2]
    #     R20, R21, R22 = o[2][0], o[2][1], o[2][2]

    #     x, y, z = self.camera.position[0]

    #     R = mm.Matrix([[R00, R01, R02, -x],
    #                   [R10, R11, R12, -y],
    #                   [R20, R21, R22, -z],
    #                   [0, 0, 0, 1]])

    #     C = mm.Matrix([[1, 0, 0, -x],
    #                    [0, 1, 0, -y],
    #                    [0, 0, 1, -z],
    #                    [0, 0, 0, 1]])


    #     return R


    def draw(self):
        """
        Loops through all the points of the shapes that have created by the user,
        then projects the points so they can be drawn on a 2d screen
        """
        self.screen.fill((255,255,255))

        for polygon in self.mesh:
            if type(polygon) == Triangle:
                for i in range(3):
                    polygon.projected_points[i] = polygon.points[i].project(self.projection_matrix(), self.camera.view_matrix())
        
                if polygon.check_projected():
                    polygon.connect_points()

            else:
                projected = polygon[0].project(self.projection_matrix(), self.camera.view_matrix())

                if projected != False:
                    x, y = projected
                    pg.draw.circle(self.screen, 0, (x, y), 3)


    # def check_movement(self):
    #     key = pg.key.get_pressed()

    #     if key[pg.K_w]:
    #         self.camera.position[0][2] -= self.z_speed
    #         #self.translate((0, 0, self.z_speed))
    #     if key[pg.K_s]:
    #         self.camera.position[0][2] += self.z_speed
    #         #self.translate((0, 0, -self.z_speed))
    #     if key[pg.K_a]:
    #         self.camera.position[0][0] += self.x_speed
    #         #self.translate((+self.x_speed, 0, 0))
    #     if key[pg.K_d]:
    #         self.camera.position[0][0] -= self.x_speed
    #         #self.translate((-self.x_speed, 0, 0))
        
    #     if key[pg.K_RIGHT]:
    #         self.camera.orientation[1] += self.angle
    #         #self.camera.rotate()
    #     if key[pg.K_LEFT]:
    #         self.camera.orientation[1] -= self.angle
    #         #self.camera.rotate()
    #     if key[pg.K_UP]:
    #         self.camera.orientation[0] += self.angle
    #         #self.camera.rotate()
    #     if key[pg.K_DOWN]:
    #         self.camera.orientation[0] -= self.angle
    #         #self.camera.rotate()
        
    #     ### mouse movement ###

    #     # mouse_x, mouse_y = pg.mouse.get_pos()
    #     # self.camera.orientation[0] += (mouse_x - self.h_width) / 100
    #     # self.camera.orientation[1] += (mouse_y - self.h_height) / 100
    #     # pg.mouse.set_pos(self.h_width, self.h_height)