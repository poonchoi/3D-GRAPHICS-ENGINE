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
    

    def connect_points(self, i, j, points):
        pg.draw.aaline(self.screen, BLACK, (points[i][0], points[i][1]), (points[j][0], points[j][1]))


    def project(self, point):
        z = 1 / (float(self.distance) - point[2])
        p = np.matrix(
            [[z, 0, 0],
            [0, z, 0],
            [0, 0, 0]]
        )
        point = np.array(point)
        projected = np.dot(p, point.reshape(3, 1))
        projected = projected.tolist()
        return [projected[0][0],projected[1][0],projected[2][0]] 


    def rotateX(self, point, angle):
        rotateX = np.matrix(
            [[1, 0, 0],
            [0, np.cos(angle), np.sin(angle)],
            [0, -np.sin(angle), np.cos(angle)]]
        )
        point = np.array(point)
        rotated = np.dot(rotateX, point.reshape(3, 1))
        rotated = rotated.tolist()
        return [rotated[0][0],rotated[1][0],rotated[2][0]]  


    def rotateY(self, point, angle):
        rotateY = np.matrix(
            [[np.cos(angle), 0, -np.sin(angle)],
            [0, 1, 0],
            [np.sin(angle), 0, np.cos(angle)]]
        )
        point = np.array(point)
        rotated = np.dot(rotateY, point.reshape(3, 1))
        rotated = rotated.tolist()
        return [rotated[0][0],rotated[1][0],rotated[2][0]] 


    def rotateZ(self, point, angle):
        rotateZ = np.matrix(
            [[np.cos(angle), np.sin(angle), 0],
            [-np.sin(angle), np.cos(angle), 0],
            [0, 0, 1]]
        )
        point = np.array(point)
        rotated = np.dot(rotateZ, point.reshape(3, 1))
        rotated = rotated.tolist()
        return [rotated[0][0],rotated[1][0],rotated[2][0]] 


    def translate(self, point, vec):
        tx, ty, tz = vec[0], vec[1], vec[2]
        translated = [point[0] + tx, point[1] + ty, point[2] + tz]
        return translated


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