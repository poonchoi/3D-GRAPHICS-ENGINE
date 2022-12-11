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

        self.f = 0.1
        self.sx = self.WIDTH / 10
        self.sy = self.HEIGHT / 10
        self.s = 0


    def connect_points(self, i, j, points):
        pg.draw.aaline(self.screen, BLACK, (points[i][0], points[i][1]), (points[j][0], points[j][1]))


    def p(self):
        p = np.matrix([[(self.f*self.WIDTH)/(2*self.sx), self.s, 0, 0],
        [0, (self.f*self.HEIGHT)/(2*self.sy), 0, 0],
        [0, 0, -1, 0],
        [0, 0, 0, 1]])
        return p


    def rx(self, angle):
        rotateX = np.matrix([[1, 0, 0, 0],
        [0, np.cos(angle), -np.sin(angle), 0],
        [0, np.sin(angle), np.cos(angle), 0]
        [0, 0, 0, 1],])
        return rotateX


    def ry(self, angle):
        rotateY = np.matrix([[np.cos(angle), np.sin(angle), 0, 0],
        [0, 1, 0, 0],
        [-np.sin(angle), np.cos(angle), 1, 0],
        [0, 0, 0, 1]])
        return rotateY


    def rz(self, angle):
        rotateZ = np.matrix([[np.cos(angle), -np.sin(angle), 0, 0],
        [np.sin(angle), np.cos(angle), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]])
        return rotateZ


    def c(self, point):
        cx = point[0]
        cy = point[1]
        cz = point[2]
        c = np.matrix([[1, 0, 0, -cx],
        [0, 1, 0, -cy],
        [0, 0, 1, -cz],
        [0, 0, 0, 1]])
        return c

    def project(self):
        result = []
        n = np.matrix([
            [1/result]
        ])


    def draw(self):
        # self.angle = pg.mouse.get_pos()[0] / 1000
        self.angle += 0.01
        self.screen.fill(WHITE)
        points = [[3, -1, 3], [5, -1, 3], [5, 1, 3], [3, 1, 3], [3, -1, -3], [5, -1, -3], [5, 1, -3], [3, 1, -3]]
        #[0,0,0],[-1,1,1],[1,1,1],[-1,-1,1],[1,-1, 1],[-1,1,-1],[1,1,-1],[-1,-1,-1],[1,-1,-1]
        projected_points = [[n, n] for n in range(len(points))]
        i = 0
        for point in points:
            rotated = self.rotateY(point, self.angle+0.01)
            #rotated = self.rotateX(rotated, self.angle)
            #rotated = self.translate(rotated, [0,0,-self.angle*5])
            projected = self.project(rotated)
            x = projected[0] * self.scale + self.H_WIDTH
            y = projected[1] * self.scale + self.H_HEIGHT
            projected_points[i] = x, y
            pg.draw.circle(self.screen, BLACK, (x, y), 2)
            i += 1

        
        for p in range(4):
            self.connect_points(p, (p+1) % 4, projected_points)
            self.connect_points(p+4, ((p+1) % 4) + 4, projected_points)
            self.connect_points(p, (p+4), projected_points) 


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