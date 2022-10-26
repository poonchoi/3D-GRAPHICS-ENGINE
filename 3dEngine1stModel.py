import pygame as pg
from pygame import gfxdraw
import numpy as np
from test2.libraryTesting.colors import *



class App:
    def __init__(self):
        pg.init()
        self.RES = self.WIDTH, self.HEIGHT = 600, 600
        self.H_WIDTH, self.H_HEIGHT = self.WIDTH // 2, self.HEIGHT // 2
        self.FPS = 10000
        self.screen = pg.display.set_mode(self.RES)
        self.clock = pg.time.Clock()
        self.angle = 0
        self.scale = 100
    

    def connect_points(self, i, j, points):
        pg.draw.aaline(self.screen, BLACK, (points[i][0], points[i][1]), (points[j][0], points[j][1]))


    def project(self, point):
        distance = 6
        z = 1 / (distance - float(point[2][0]))
        p = np.matrix(
            [[z, 0, 0],
            [0, z, 0],
            [0, 0, 0]]
        )
        point = np.array(point)
        projected = np.dot(p, point.reshape(3, 1))
        projected = projected.tolist()
        return projected


    def rotateX(self, point, angle):
        rotateX = np.matrix(
            [[1, 0, 0],
            [0, np.cos(angle), np.sin(angle)],
            [0, -np.sin(angle), np.cos(angle)]]
        )
        point = np.array(point)
        rotated = np.dot(rotateX, point.reshape(3, 1))
        rotated = rotated.tolist()
        return rotated


    def rotateY(self, point, angle):
        rotateY = np.matrix(
            [[np.cos(angle), 0, -np.sin(angle)],
            [0, 1, 0],
            [np.sin(angle), 0, np.cos(angle)]]
        )
        point = np.array(point)
        rotated = np.dot(rotateY, point.reshape(3, 1))
        rotated = rotated.tolist()
        return rotated


    def rotateZ(self, x, angle):
        rotateZ = np.matrix(
            [[np.cos(angle), np.sin(angle), 0],
            [-np.sin(angle), np.cos(angle), 0],
            [0, 0, 1]]
        )
        x = np.array(x)
        rotated = np.dot(rotateZ, x.reshape(3, 1))
        rotated = rotated.tolist()
        return rotated


    def draw(self):
        # self.angle = pg.mouse.get_pos()[0] / 1000
        self.angle += 0.001
        self.screen.fill(WHITE)
        points = [[-1, -1, 3], [1, -1, 3], [1, 1, 3], [-1, 1, 3], [-1, -1, -3], [1, -1, -3], [1, 1, -3], [-1, 1, -3]]
        projected_points = [[n, n] for n in range(len(points))]
        i = 0
        for point in points:
            rotated = self.rotateY(point, self.angle+0.01)
            rotated = self.rotateX(rotated, self.angle)
            rotated = self.rotateZ(rotated, -self.angle)
            projected = self.project(rotated)
            x = projected[0][0] * self.scale + self.H_WIDTH
            y = projected[1][0] * self.scale + self.H_HEIGHT
            projected_points[i] = x, y
            #pg.draw.circle(self.screen, BLACK, (x, y), 5)
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