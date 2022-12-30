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
        self.camera = [0, 0, 0]

        self.movement_speed = 1
        self.angle = m.radians(1)

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


    def draw(self):
        """
        Loops through all the points of the shapes that have created by the user,
        then projects the points so they can be drawn on a 2d screen
        """
        self.screen.fill(0)
        for shape in self.all_shapes:
            for point in shape: # only draw point if z coordinate is in front of camera
                projected = point.project(self.camera)
                if projected != False:
                    x, y, z = projected
                    pg.draw.circle(self.screen, (0,255,0), (x + self.h_width, y + self.h_height), 1)


    def check_movement(self):
        key = pg.key.get_pressed()

        if key[pg.K_w]:
            #self.camera[2] -= self.movement_speed
            self.translate((0, 0, self.movement_speed))
        if key[pg.K_s]:
            #self.camera[2] += self.movement_speed
            self.translate((0, 0, -self.movement_speed))
        if key[pg.K_a]:
            #self.camera[0] += self.movement_speed
            self.translate((-self.movement_speed, 0, 0))
        if key[pg.K_d]:
            #self.camera[0] -= self.movement_speed
            self.translate((self.movement_speed, 0, 0))
        
        if key[pg.K_RIGHT]:
            for shape in self.all_shapes:
                for point in shape:
                    point.rotate_y(self.angle)
        if key[pg.K_LEFT]:
            for shape in self.all_shapes:
                for point in shape:
                    point.rotate_y(-self.angle)
        if key[pg.K_UP]:
            for shape in self.all_shapes:
                for point in shape:
                    point.rotate_x(self.angle)
        if key[pg.K_DOWN]:
            for shape in self.all_shapes:
                for point in shape:
                    point.rotate_x(-self.angle)




class Point():
    def __init__(self, app, coordinate):
        self.coordinate = Matrix([coordinate])
        self.in_view = True
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
    
    def infront_of_cam(self, cam):
        if self[2] >= cam[2]:
            self.in_view = False
        else: 
            self.in_view = True


    def cam_translate(self, cam):
        """
        corrects the point so that the camera is in the middle of the coordinate space
        """
        xc, yc, zc = cam[0], cam[1], cam[2]
        x, y, z = self.coordinate[0]
        point = Matrix([[x-xc, y-yc, z-zc]])
        return point


    def project(self, camera):
        #self.infront_of_cam(camera)
        if self.in_view == True:
            translated_point = self.cam_translate(camera)
            d = -translated_point[0][2]
            z = 1/(d+0.00000000000000001)
            projection_matrix = Matrix([[1, 0, 0],
                                        [0, 1, 0],
                                        [0, 0, 0]])
            # projection_matrix = Matrix([[z, 0, 0],
            #                             [0, z, 0],
            #                             [0, 0, 0]])
            new_point = translated_point * projection_matrix
            return new_point[0]
        else:
            return False


    def rotate_x(self, angle):
        """
        rotates point in x axis by given angle
        """
        rotateX = Matrix([[1, 0, 0],
                          [0, m.cos(angle), m.sin(angle)],
                          [0, -m.sin(angle), m.cos(angle)]])
        
        self.coordinate *= rotateX


    def rotate_y(self, angle):
        """
        rotates point in y axis by given angle
        """
        rotateY = Matrix([[m.cos(angle), 0, -m.sin(angle)],
                          [0, 1, 0],
                          [m.sin(angle), 0, m.cos(angle)]])

        self.coordinate *= rotateY


    def rotate_z(self, angle):
        """
        rotates point in z axis by given angle
        """
        rotateZ = Matrix([[m.cos(angle), -m.sin(angle), 0],
                          [m.sin(angle), m.cos(angle), 0],
                          [0, 0, 1]])

        self.coordinate *= rotateZ