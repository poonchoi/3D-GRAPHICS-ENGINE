import pygame as pg
from pg3dmarch.camera import Camera
from pg3dmarch.projection import Projection
import numpy as np


class App:
    def __init__(self, dimensions):
        """
        creates all necessary pygame variables and instantiates World class
        """
        pg.init()
        self.res = self.width, self.height = dimensions
        self.h_width, self.h_height = self.width // 2, self.height // 2
        self.fps = 60
        self.screen = pg.display.set_mode(self.res)
        self.clock = pg.time.Clock()

        self.camera = Camera(self)
        self.projection = Projection(self)

        self.mesh = [[np.matrix([[50,50,0,1]]), np.matrix([[50,50,3,1]]), 
                      np.matrix([[-50,-50,0,1]]), np.matrix([[-50,-50,3,1]]), 
                      np.matrix([[50,-50,0,1]]), np.matrix([[50,-50,3,1]]), 
                      np.matrix([[-50,50,0,1]]), np.matrix([[-50,50,3,1]])]]
        self.projected_mesh = []

    def project(self):
        self.projected_mesh = []

        for shape in self.mesh:
            for point in shape:
                pointI = point @ self.camera.camera_matrix() 
                pointII = pointI @ self.projection.projection_matrix
                x, y, z, w = pointII[0]

            shape[(shape > 2) | (shape < -2)] = 0


    def draw(self):
        self.screen.fill((255, 255, 255))
        self.project()
        for point in self.projected_mesh:
            pg.draw.circle(self.screen, (0, 0, 0), (point[0]+self.h_width, point[1]+self.h_height), 5)


    def run(self):
        """
        The main loop of the program
        """
        while True:
            self.camera.check_movement()
            self.draw()

            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            pg.display.set_caption(f"{round(self.clock.get_fps())} FPS")
            pg.display.flip()
            self.clock.tick(self.fps)