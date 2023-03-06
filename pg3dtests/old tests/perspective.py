import pygame as pg
from pg3d.MatrixMath.matrix import Matrix
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
        self.camera_pos = [0, 0, -100]

        self.movement_speed = 5
        self.angleX = m.radians(1)
        self.angleY = m.radians(1)
        self.angleZ = m.radians(1)

        self.dimensions = dimensions
        self.h_width = dimensions[0] // 2
        self.h_height = dimensions[1] // 2
        self.screen = screen

        self.all_shapes = []


    def add_point(self, point):
        self.all_shapes.append([point])


    def add_shape(self, shape):
        self.all_shapes.append(shape)


    def translate(self, new_pos):
        """
        moves point by given values in x, y & z
        """
        x, y, z = new_pos
        for shape in self.all_shapes:
            for point in shape:
                point[0] += x
                point[1] += y
                point[2] += z


    def check_movement(self):
        """
        checks if the user presses a key and does the corresponding actions
        """
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
        
        if key[pg.K_RIGHT]:
            for shape in self.all_shapes:
                for point in shape:
                    point.project(1, self.dimensions[0], self.dimensions[1], 0, self.camera_pos, 0, self.angleY, 0)
        elif key[pg.K_LEFT]:
            for shape in self.all_shapes:
                for point in shape:
                    point.project(1, self.dimensions[0], self.dimensions[1], 0, self.camera_pos, 0, self.angleY, 0)
        elif key[pg.K_UP]:
            for shape in self.all_shapes:
                for point in shape:
                    point.project(1, self.dimensions[0], self.dimensions[1], 0, self.camera_pos, self.angleX, 0, 0)
        elif key[pg.K_DOWN]:
            for shape in self.all_shapes:
                for point in shape:
                    point.project(1, self.dimensions[0], self.dimensions[1], 0, self.camera_pos, self.angleX, 0, 0)
        else:
            for shape in self.all_shapes:
                for point in shape:
                    point.project(1, self.dimensions[0], self.dimensions[1], 0, self.camera_pos, 0, 0, 0)


    def draw(self):
        """
        Loops through all the points of the shapes that have created by the user,
        then projects the points so they can be drawn on a 2d screen
        """
        self.screen.fill(0)
        for shape in self.all_shapes:
            for point in shape: # only draw point if z coordinate is in front of camera
                x, y, z = point[0], point[1], point[3]
                print(point)
                # x /= z
                # y /= z
                pg.draw.circle(self.screen, (0,255,0), (x + self.h_width, y + self.h_height), 3)




class Point():
    def __init__(self, app, coordinate):
        self.coordinate = Matrix([coordinate])
        app.add_point(self)


    def __repr__(self):
        return str(self.coordinate[0])


    def __setitem__(self, index, value):
        self.coordinate[0][index] = value


    def __getitem__(self, item):
        if item == 0 or item == 1 or item == 2:
            return self.coordinate[0][item]
        else:
            return "invalid"
    

    def project(self, f, w, h, skew, cam, angleX, angleY, angleZ):
        px, py = w / 1000, h / 1000
        m00 = (f * w) / (2 * px)
        m01 = skew
        m11 = (f * h) / (2 * py)
        projection = Matrix([[m00, m01, 0, 0],
                             [0, m11, 0, 0],
                             [0, 0, 1, 0],
                             [0, 0, 0, 1]])

        new_point = self.coordinate * projection * self.rotate_x(angleX) * self.rotate_y(angleY) * self.rotate_z(angleZ) * self.camera_translate(cam)
        self.coordinate = new_point

    def camera_translate(self, cam):
        translation = Matrix([[1, 0, 0, -cam[0]],
                              [0, 1, 0, -cam[1]],
                              [0, 0, 1, -cam[2]],
                              [0, 0, 0, 1]])
        return translation

    def rotate_x(self, angle):
        """
        rotates point in x axis by given angle
        """
        rotateX = Matrix([[1, 0, 0, 0],
                          [0, m.cos(angle), m.sin(angle), 0],
                          [0, -m.sin(angle), m.cos(angle), 0],
                          [0, 0, 0, 1]])
        return rotateX


    def rotate_y(self, angle):
        """
        rotates point in y axis by given angle
        """
        rotateY = Matrix([[m.cos(angle), 0, -m.sin(angle), 0],
                          [0, 1, 0, 0],
                          [m.sin(angle), 0, m.cos(angle), 0],
                          [0, 0, 0, 1]])
        return rotateY


    def rotate_z(self, angle):
        """
        rotates point in z axis by given angle
        """
        rotateZ = Matrix([[m.cos(angle), -m.sin(angle), 0, 0],
                          [m.sin(angle), m.cos(angle), 0, 0],
                          [0, 0, 1, 0],
                          [0, 0, 0, 1]])
        return rotateZ