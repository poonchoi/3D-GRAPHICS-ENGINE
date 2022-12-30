import pygame as pg
import math as m
from pg3d.MatrixMath.matrix import Matrix
from pg3d.camera import Camera
from pg3d.triangle import Triangle
from pg3d.point import Point


class World():
    def __init__(self, dimensions, screen, app):
        self.app = app
        self.camera = Camera([0, 0, 0])

        self.z_speed = 0.07
        self.x_speed = 1.8
        self.angle = .5

        self.dimensions = dimensions
        self.width = dimensions[0]
        self.height = dimensions[1]
        self.h_width = self.width // 2
        self.h_height = self.height // 2
        self.screen = screen

        self.mesh = []

        self.n = 0.1
        self.f = 1000
        self.fov = 90
        self.a = self.width / self.height


    def add_point(self, point):
        self.mesh.append([point])


    def add_triangle(self, triangle):
        self.mesh.append(triangle)


    def translate(self, new_pos):
        """
        moves point by given values in x, y & z
        """
        x, y, z = new_pos
        for polygon in self.mesh:
            for point in polygon:
                point[0] += x
                point[1] += y
                point[2] += z
    

    def projection_matrix(self):
        n = self.n
        f = self.f
        fov = self.fov
        a = self.a

        fov_rad = m.radians(fov)
        t = m.tan(fov_rad / 2) * n
        b = -t
        r = t * a
        l = -r

        return Matrix([[(2*n)/(r-l), 0, (r+l)/(r-l), 0],
                       [0, (2*n)/(t-b), (t+b)/(t-b), 0],
                       [0, 0, -(f+n)/(f-n), -(2*f*n)/(f-n)],
                       [0, 0, 1, 0]])


    def view_matrix(self):
        pitch, yaw = m.radians(self.camera.orientation[0]), m.radians(self.camera.orientation[1])

        y_rot = Matrix([[m.cos(yaw), 0, m.sin(yaw)],
                        [0, 1, 0],
                        [-m.sin(yaw), 0, m.cos(yaw)]])

        x_rot = Matrix([[1, 0, 0],
                        [0, m.cos(pitch), -m.sin(pitch)],
                        [0, m.sin(pitch), m.cos(pitch)]])

        o = y_rot * x_rot

        R00, R01, R02 = o[0][0], o[0][1], o[0][2]
        R10, R11, R12 = o[1][0], o[1][1], o[1][2]
        R20, R21, R22 = o[2][0], o[2][1], o[2][2]

        x, y, z = self.camera.position

        return Matrix([[R00, R01, R02, -x],
                       [R10, R11, R12, -y],
                       [R20, R21, R22, -z],
                       [0, 0, 0, 1]])


    def draw(self):
        """
        Loops through all the points of the shapes that have created by the user,
        then projects the points so they can be drawn on a 2d screen
        """
        self.screen.fill(0)

        for polygon in self.mesh:

            if type(polygon) == Triangle:
                for i in range(3):
                    polygon.projected_points[i] = polygon.points[i].project(self.projection_matrix(), self.view_matrix())
        
                if polygon.check_projected():
                    polygon.connect_points()

            else:
                projected = polygon[0].project(self.projection_matrix(), self.view_matrix())

                if projected != False:
                    x, y = projected
                    pg.draw.circle(self.screen, (0,255,0), (x, y), 1)


    def check_movement(self):
        key = pg.key.get_pressed()

        if key[pg.K_w]:
            #self.camera.position[2] += self.z_speed
            self.translate((0, 0, self.z_speed))
        if key[pg.K_s]:
            #self.camera.position[2] -= self.z_speed
            self.translate((0, 0, -self.z_speed))
        if key[pg.K_a]:
            #self.camera.position[0] += self.x_speed
            self.translate((+self.x_speed, 0, 0))
        if key[pg.K_d]:
            #self.camera.position[0] -= self.x_speed
            self.translate((-self.x_speed, 0, 0))
        
        if key[pg.K_RIGHT]:
            self.camera.orientation[1] += self.angle
        if key[pg.K_LEFT]:
            self.camera.orientation[1] -= self.angle
        if key[pg.K_UP]:
            self.camera.orientation[0] += self.angle
        if key[pg.K_DOWN]:
            self.camera.orientation[0] -= self.angle
        
        ### mouse movement ###

        # mouse_x, mouse_y = pg.mouse.get_pos()
        # self.camera.orientation[0] += mouse_x - self.h_width
        # self.camera.orientation[1] += mouse_y - self.h_height
        # pg.mouse.set_pos(self.h_width, self.h_height)