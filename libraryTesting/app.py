import pygame
import numpy as np
from colors import *
from matrices import *
from cube import Cube


class App():
    def __init__(self, resolution=(800, 600)):
        pygame.init()
        self.RES = self.WIDTH, self.HEIGHT = (resolution)
        self.H_WIDTH, self.H_HEIGHT = self.WIDTH // 2, self.HEIGHT // 2
        self.FPS = 600
        self.screen = pygame.display.set_mode(self.RES)
        self.clock = pygame.time.Clock()

        self.angle = 0
        self.scale = 200


    def connect_points(self, i, j, points):
        pygame.draw.line(self.screen, BLACK, (points[i][0], points[i][1]), (points[j][0], points[j][1]))


    def draw(self):
        pass


    def run(self):
        while True:
            self.draw()

            [exit() for i in pygame.event.get() if i.type == pygame.QUIT]
            pygame.display.set_caption(f"{round(self.clock.get_fps())} FPS")
            pygame.display.flip()
            self.clock.tick(self.FPS)


if __name__ == '__main__':
    app = App()
    app.run()