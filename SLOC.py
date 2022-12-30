import pygame as pg
import math as m
from pygame3D.MatrixMath.matrix import Matrix



class App:
    def __init__(self, dimensions):
        """
        creates all necessary pygame variables and instantiates World class
        """
        pg.init()
        self.RES = self.WIDTH, self.HEIGHT = dimensions
        self.H_WIDTH, self.H_HEIGHT = self.WIDTH // 2, self.HEIGHT // 2
        self.FPS = 60
        self.screen = pg.display.set_mode(self.RES)
        self.clock = pg.time.Clock()
        self.world = World(self.RES, self.screen, self)


    def add_point(self, point):
        self.world.add_point(point)
    
    
    def add_triangle(self, triangle):
        self.world.add_triangle(triangle)


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


class Camera():
    def __init__(self, position):
        self.position = position
        self.orientation = [0, 0]


class Point():
    def __init__(self, app, coordinate, vertex=False):
        self.coordinate = Matrix([coordinate])
        if not vertex:
            app.add_point(self)
        self.app = app
        self.world = app.world


    def __repr__(self):
        return str(self.coordinate[0])


    def __setitem__(self, index, value):
        self.coordinate[0][index] = value


    def __getitem__(self, item):
        if item == 0 or item == 1 or item == 2:
            return self.coordinate[0][item]

        else:
            return "invalid"

    
    def project(self, P, V):
        projected = P * V.inverse() * self.coordinate

        if not projected[0][3] <= 0:
            x = (projected[0][0] / projected[0][3]) + self.app.H_WIDTH
            y = (projected[0][1] / projected[0][3]) + self.app.H_HEIGHT
            return x, y

        else:
            return None


class Triangle:
    def __init__(self, app, a, b, c):
        self.points = [Point(app, a, True), Point(app, b, True), Point(app, c, True)]
        self.projected_points = [[None] for i in range(3)]
        self.app = app
        app.add_triangle(self)

    def connect_points(self):
        print(self.projected_points)
        pg.draw.polygon(self.app.screen, (255,255,255), self.projected_points)

    def check_projected(self):
        for i in range(2):
            if None in self.projected_points[i]:
                self.projected_points[i]
                return False
    
    def __getitem__(self, index):
        return self.points[index]


class World():
    def __init__(self, dimensions, screen, app):
        self.app = app
        self.camera = Camera([0, 0, 0])

        self.z_speed = 0.07
        self.x_speed = 1.8
        self.angle = .5

        self.dimensions = dimensions
        self.h_width = dimensions[0] // 2
        self.h_height = dimensions[1] // 2
        self.screen = screen

        self.mesh = []

        self.n = 0.1
        self.f = 1000
        self.fov = 90
        self.a = dimensions[0] / dimensions[1]


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
                for i in range(2):
                    print(polygon.points[i].project(self.projection_matrix(), self.view_matrix()))
                    polygon.projected_points[i] = polygon.points[i].project(self.projection_matrix(), self.view_matrix())
        
                if polygon.check_projected():
                    print(polygon.check_projected())
                    polygon.connect_points()

            elif type(polygon) == Point:
                projected = polygon[0].project(self.projection_matrix(), self.view_matrix())

                if projected != None:
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