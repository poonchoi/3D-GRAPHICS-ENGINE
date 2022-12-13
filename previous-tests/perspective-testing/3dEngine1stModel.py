import pygame as pg
from pygame import gfxdraw
import numpy as np
BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)


class App:
    def __init__(self):
        pg.init()
        self.RES = self.WIDTH, self.HEIGHT = 600, 600
        self.H_WIDTH, self.H_HEIGHT = self.WIDTH // 2, self.HEIGHT // 2
        self.FPS = 100
        self.screen = pg.display.set_mode(self.RES)
        self.clock = pg.time.Clock()
        self.angle = 0
        self.scale = 100
        self.distance = 9

        self.w, self.h = 600, 600
        self.cam = np.array([0,0,0,1])
        self.rot = np.array([0,0,0])
        self.f = 0.1
        self.px, self.py = self.w/1000, self.h/1000
        self.offx, self.offy = self.w/2, self.h/2
        self.pix = 12
        self.skew = 0


    def connect_points(self, i, j, points):
        pg.draw.aaline(self.screen, BLACK, (points[i][0], points[i][1]), (points[j][0], points[j][1]))


    def p(self):
        p = np.array([
            [(self.f*self.w)/(2*self.px),self.skew,0,0],
            [0,(self.f*self.h)/(2*self.py),0,0],
            [0,0,-1,0],
            [0,0,0,1]
        ])
        return p


    def rx(self):
        rx = np.array([
            [1,0,0,0],
            [0,np.cos(self.rot[0]),-np.sin(self.rot[0]),0],
            [0,np.sin(self.rot[0]),np.cos(self.rot[0]),0],
            [0,0,0,1]
        ])
        return rx


    def ry(self):
        ry = np.array([
            [np.cos(self.rot[1]),0,np.sin(self.rot[1]),0],
            [0,1,0,0],
            [-np.sin(self.rot[1]),0,np.cos(self.rot[1]),0],
            [0,0,0,1]
        ])
        return ry


    def rz(self):
        rz = np.array([
            [np.cos(self.rot[2]),-np.sin(self.rot[2]),0,0],
            [np.sin(self.rot[2]),np.cos(self.rot[2]),0,0],
            [0,0,1,0],
            [0,0,0,1]
        ])
        return rz


    def g(self, point):
        G = np.array([
            [1,0,0,-point[0]],
            [0,1,0,-point[1]],
            [0,0,1,-point[2]],
            [0,0,0,1]
        ])

        return G


    def project(self, point):
        new_point = point @ self.p() @ self.rx() @ self.ry() @ self.rx() @ self.g(point)
        proj = [None, None]
        proj[0] = new_point[0] / new_point[3]
        proj[1] = new_point[1] / new_point[3]


    def draw(self):
        self.screen.fill(WHITE)
        points = [[0,0,0,1],[-1,1,1,1],[1,1,1,1],[-1,-1,1,1],[1,-1, 1,1],[-1,1,-1,1],[1,1,-1,1],[-1,-1,-1,1],[1,-1,-1,1]]
        #[0,0,0],[-1,1,1],[1,1,1],[-1,-1,1],[1,-1, 1],[-1,1,-1],[1,1,-1],[-1,-1,-1],[1,-1,-1]
        for point in points:
            projected = self.project(point)
            x, y = projected[0], projected[1]
            pg.draw.circle(self.screen, BLACK, (x, y), 2)


    def run(self):
        while True:
            self.draw()

            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            pg.display.set_caption(f"{round(self.clock.get_fps())} FPS")
            pg.display.flip()
            self.clock.tick(self.FPS)


if __name__ == '__main__':
    app = App()
    app.run()