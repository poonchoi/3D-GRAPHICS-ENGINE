import pygame as pg
import math as m
import pg3dFINAL.MatrixMath.matrix as mm
from pg3dFINAL.camera import Camera
from pg3dFINAL.triangle import Triangle
from pygame.colordict import THECOLORS


class App:
    def __init__(self, dimensions=(1000, 700), cam_pos=[0,0,0], bg_color=(0,0,0), line_color=(255,255,255), vertex_size=2):
        pg.init()
        self.res = self.width, self.height = dimensions
        self.hwidth, self.hheight = self.width / 2, self.height / 2
        self.fps = 60
        self.screen = pg.display.set_mode(self.res)
        self.clock = pg.time.Clock()

        self.bg_color = bg_color
        self.line_color = line_color
        self.vertex_size = vertex_size

        self.camera = Camera(self, cam_pos)

        self.mesh = []

        self.fov = 90
        self.f = 1 / m.tan(m.radians(self.fov / 2))
        self.zf = 1000
        self.zn = .1
        self.g = self.zf / (self.zf - self.zn)
        self.a = self.height / self.width

        m00 = self.a * self.f
        m11 = self.f
        m22 = self.g
        m32 = -self.zn * self.g
        
        self.projection_mat = mm.Matrix([[m00, 0, 0, 0],
                                         [0, m11, 0, 0],
                                         [0, 0, m22, 1],
                                         [0, 0, m32, 0]])


    def add_point(self, point):
        self.mesh.append([point])


    def add_triangle(self, triangle):
        self.mesh.append(triangle)


    def draw(self):
        self.screen.fill(self.bg_color)
        for shape in self.mesh:
            if type(shape) == Triangle:
                shape.project()
            else:
                for point in shape:
                    projected = point.project(self.projection_mat, self.camera.cam_mat())
                    if projected != None:
                        x, y, z = projected
                        pg.draw.circle(self.screen, self.line_color, (x, y), self.vertex_size)


    def run(self):
        while True:
            self.draw()
            self.camera.movement()

            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            pg.display.set_caption(f"{round(self.clock.get_fps())} FPS")
            pg.display.flip()
            self.clock.tick(self.fps)