import pygame as pg
import math as m
import pg3dFINAL.MatrixMath.matrix as mm
from pg3dFINAL.camera import Camera
from pygame.colordict import THECOLORS


class App:
    def __init__(self, dimensions, cam_pos=[0,0,0]):
        pg.init()
        self.res = self.width, self.height = dimensions
        self.hwidth, self.hheight = self.width / 2, self.height / 2
        self.fps = 60
        self.screen = pg.display.set_mode(self.res)
        self.clock = pg.time.Clock()

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
        self.screen.fill(THECOLORS["cornsilk4"])
        for shape in self.mesh:
            for point in shape:
                point.project(self.projection_mat, self.camera.cam_mat())


    def run(self):
        while True:
            self.draw()
            self.camera.movement()

            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            pg.display.set_caption(f"{round(self.clock.get_fps())} FPS")
            pg.display.flip()
            self.clock.tick(self.fps)



if __name__ == "__main__":
    app = App()
    app.run()