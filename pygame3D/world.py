from MatrixMath.matrix import Matrix
import pygame as pg
import math as m


class World():
    def __init__(self, dimensions, screen):
        self.dimensions = dimensions
        self.h_width = dimensions[0] // 2
        self.h_height = dimensions[1] // 2
        self.screen = screen
        self.all_shapes = []
        self._PROJECT_MATRIX = Matrix([[1, 0, 0],
                                        [0, 1, 0],
                                        [0, 0, 0]])


    def add_point(self, point):
        self.all_shapes.append([point])


    def add_shape(self, shape):
        self.all_shapes.append(shape)


    def project(self, point):
        return point * self._PROJECT_MATRIX


    def rotate_x(self, angle, point):
        rotateX = Matrix([[1, 0, 0],
                          [0, m.cos(angle), m.sin(angle)],
                          [0, -m.sin(angle), m.cos(angle)]])
        return point * rotateX


    def rotate_y(self, angle, point):
        rotateY = Matrix([[m.cos(angle), 0, -m.sin(angle)],
                          [0, 1, 0],
                          [m.sin(angle), 0, m.cos(angle)]])
        return point * rotateY


    def rotate_z(self, angle, point):
        rotateZ = Matrix([[m.cos(angle), m.sin(angle), 0],
                          [-m.sin(angle), m.cos(angle), 0],
                          [0, 0, 1]])
        return point * rotateZ


    def translate(self, new_pos, point):
        x, y, z = new_pos
        translate = Matrix([[x, 0, 0],
                            [0, y, 0],
                            [0, 0, z]])
        return point * translate


    def draw(self):
        projected_points = [[n, n] for n in range(len(self.all_shapes))]
        for shape in self.all_shapes:
            for point in shape:
                # projected_points[shape][point] = self.project(point)
                projected = point.project()
                x, y, z = projected
                pg.draw.circle(self.screen, (0,255,0), (x + self.h_width, y + self.h_height), 6)


    def check_movement(self):
        key = pg.key.get_pressed()


    def run(self):
        pass