import pygame as pg
import numpy as np
from test2.libraryTesting.colors import *
import math



class App:
    def __init__(self):
        pg.init()
        self.RES = self.WIDTH, self.HEIGHT = 600, 600
        self.H_WIDTH, self.H_HEIGHT = self.WIDTH // 2, self.HEIGHT // 2
        self.FPS = 60
        self.screen = pg.display.set_mode(self.RES)
        self.clock = pg.time.Clock()
        self.angle = 0
        self.scale = 10
    

    def connect_points(self, i, j, points):
        pg.draw.line(self.screen, BLACK, (points[i][0], points[i][1]), (points[j][0], points[j][1]))


    def project(self, point):
        zfar = 10
        znear = 1
        fov = 60
        a = self.WIDTH / self.HEIGHT
        f = 1/math.tan(fov * 0.5 / 180 * math.pi)
        q = zfar/(zfar-znear)
        b = (-zfar*znear)/(zfar-znear)
        c = (-znear-zfar)/(znear-zfar)
        d = (2*zfar*znear)/(znear-zfar)
        p = np.matrix([
            [a*f,0,0,0],
            [0,f,0,0],
            [0,0,c,d],
            [0,0,-1,0]
        ])

        point = np.array(point)
        projected = np.matmul(p, point.reshape(4,1))
        projected = projected.tolist()
        print(projected)
        projected[0][0] = projected[0][0] / projected[3][0]
        projected[1][0] = projected[1][0] / projected[3][0]
        projected[2][0] = projected[2][0] / projected[3][0]
        projected = [projected[0][0], projected[1][0], projected[2][0]]
        # projected[0] *= self.WIDTH
        # projected[1] *= self.HEIGHT
        # projected[2] += 10
        projected[0] = ((projected[0]*self.WIDTH) / (2*self.WIDTH) + self.H_WIDTH)
        projected[1] = ((projected[0]*self.HEIGHT) / (2*self.WIDTH) + self.H_HEIGHT)
        return projected


    def draw(self):
        self.screen.fill(WHITE)
        points = [[-1, -1, 1, 1], [1, -1, 1, 1], [1, 1, 1, 1], [-1, 1, 1, 1], [-1, -1, -1, 1], [1, -1, -1, 1], [1, 1, -1, 1], [-1, 1, -1, 1]]
        for point in points:
            print(point)
            x, y, z = self.project(point)
            print(x,y,z)
            pg.draw.circle(self.screen, BLACK, (x, y), 1)


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