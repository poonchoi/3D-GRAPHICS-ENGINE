from MatrixMath.matrix import Matrix
import pygame as pg
import math as m


class World:
    def __init__(self, dimensions=(100,100)):
        self.dimnesions = dimensions
        self.all_shapes = []
        self.__PROJECT_MATRIX = Matrix([[1, 0, 0],
                                        [0, 1, 0]
                                        [0, 0, 0]])

    
    def add_point(self, point):
        self.all_shapes.append([point])


    def add_shape(self, shape):
        self.all_shapes.append(shape)


    def project(self):
        projected_points = [[n, n] for n in range(len(self.self.all_shapes))]
        for shape in self.all_shapes:
            for point in shape:
                projected_points
                
        return point * self.__PROJECT_MATRIX

    
    def rotate_x(self, angle):
        rotateX = Matrix([[1, 0, 0],
                          [0, m.cos(angle), m.sin(angle)],
                          [0, -m.sin(angle), m.cos(angle)]])


    def rotate_y(self, angle):
        rotateY = Matrix([[m.cos(angle), 0, -m.sin(angle)],
                             [0, 1, 0],
                             [m.sin(angle), 0, m.cos(angle)]])


    def rotate_z(self, angle):
        rotateZ = Matrix([[m.cos(angle), m.sin(angle), 0],
                          [-m.sin(angle), m.cos(angle), 0],
                          [0, 0, 1]])


    def translate(self, new_pos):
        pass


    def draw(self):
        pass


    def check_movement(self):
        pass


    def run(self):
        pass