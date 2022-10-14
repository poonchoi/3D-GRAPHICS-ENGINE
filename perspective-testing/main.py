import pygame as pg
import numpy as np
from test2.libraryTesting.colors import *


class App:
    def __init__(self):
        pg.init()
        self.RES = self.WIDTH, self.HEIGHT = 600, 600
        self.H_WIDTH, self.H_HEIGHT = self.WIDTH // 2, self.HEIGHT // 2
        self.FPS = 60
        self.screen = pg.display.set_mode(self.RES)
        self.clock = pg.time.Clock()

    def perspective_p(self):
        fov = 80
        s = 1 / np.tan((fov/2)*(np.pi/180))
        f = 5
        n = 1
        matrix = [
            [s, 0, 0, 0],
            [0, s, 0, 0],
            [0, 0, -f/(f-n), -1],
            [0, 0, -(f*n)/(f-n), 0]
        ]

    def draw(self):
        pass


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