import pygame as pg
from pygame3D.MatrixMath.matrix import Matrix
import math as m


class App:
    def __init__(self, dimensions):
        """
        creates all necessary pygame variables and instantiates World class
        """
        pg.init()
        self.RES = self.WIDTH, self.HEIGHT = dimensions
        self.H_WIDTH, self.H_HEIGHT = self.WIDTH // 2, self.HEIGHT // 2
        self.FPS = 100
        self.screen = pg.display.set_mode(self.RES)
        self.clock = pg.time.Clock()
        self.world = World(self.RES, self.screen, self)

    def add_point(self, point):
        self.world.add_point(point)


    def run(self):
        """
        the main loop
        """
        while True:
            self.world.check_movement()
            self.world.draw()

            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            pg.display.set_caption(f"{round(self.clock.get_fps())} FPS")
            pg.display.flip()
            self.clock.tick(self.FPS)




class World():
    def __init__(self, dimensions, screen, app):
        self.app = app
        self.camera_pos = [0, 0, 0]
        self.movement_speed = 5
        self.angle = 0
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


    def rotate_x(self):
        """
        rotates point in x axis by given angle
        """
        rotateX = Matrix([[1, 0, 0],
                          [0, m.cos(self.angle), m.sin(self.angle)],
                          [0, -m.sin(self.angle), m.cos(self.angle)]])
        for shape in self.all_shapes:
            for point in shape:
                self.all_shapes[shape][point] = point * rotateX


    def rotate_y(self):
        """
        rotates point in y axis by given angle
        """
        rotateY = Matrix([[m.cos(self.angle), 0, -m.sin(self.angle)],
                          [0, 1, 0],
                          [m.sin(self.angle), 0, m.cos(self.angle)]])
        for shape in self.all_shapes:
            for point in shape:
                self.all_shapes[shape][point] = point * rotateY


    def rotate_z(self):
        """
        rotates point in z axis by given angle
        """
        rotateZ = Matrix([[m.cos(self.angle), m.sin(self.angle), 0],
                          [-m.sin(self.angle), m.cos(self.angle), 0],
                          [0, 0, 1]])
        for shape in self.all_shapes:
            for point in shape:
                self.all_shapes[shape][point] = point * rotateZ


    def translate(self, new_pos):
        """
        moves point by given values in x, y & z
        """
        x, y, z = new_pos
        for shape in self.all_shapes:
            for point in shape:
                point[0] = x
                point[1] = x
                point[1] = x


    def draw(self):
        """
        Loops through all the points of the shapes that have created by the user,
        then projects the points so they can be drawn on a 2d screen
        """
        for shape in self.all_shapes:
            for point in shape: # only draw point if z coordinate is in front of camera
                projected = point.project()
                x, y, z = projected
                pg.draw.circle(self.screen, (0,255,0), (x + self.h_width, y + self.h_height), 6)


    def check_movement(self):
        key = pg.key.get_pressed()
        if key[pg.K_w]:
            self.camera_pos[2] += self.movement_speed
            self.translate((0, 0, self.movement_speed))
        if key[pg.K_s]:
            self.camera_pos[2] -= self.movement_speed
            self.translate((0, 0, -self.movement_speed))
        if key[pg.K_a]:
            self.camera_pos[0] -= self.movement_speed
            self.translate((-self.movement_speed, 0, 0))
        if key[pg.K_d]:
            self.camera_pos[0] += self.movement_speed
            self.translate((self.movement_speed, 0, 0))




class Point():
    projection_matrix = Matrix([[1, 0, 0],
                                [0, 1, 0],
                                [0, 0, 0]])


    def __init__(self, app, coordinate):
        self.coordinate = Matrix([coordinate])
        app.add_point(self)
    

    def project(self):
        new_point = self.coordinate * Point.projection_matrix
        return new_point[0]


    def __repr__(self):
        return str(self.coordinate[0])


    def __getitem__(self, item):
        if item == 0 or item == 1 or item == 2:
            return self.coordinate[0][item]
        else:
            return "invalid"