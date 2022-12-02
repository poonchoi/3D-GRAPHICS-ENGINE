import pygame as pg
from world import World


class App:
    def __init__(self, dimensions):
        pg.init()
        self.RES = self.WIDTH, self.HEIGHT = dimensions
        self.H_WIDTH, self.H_HEIGHT = self.WIDTH // 2, self.HEIGHT // 2
        self.FPS = 100
        self.screen = pg.display.set_mode(self.RES)
        self.clock = pg.time.Clock()
        self.world = World(self.RES)


    def run(self):
        while True:
            World.draw()

            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            pg.display.set_caption(f"{round(self.clock.get_fps())} FPS")
            pg.display.flip()
            self.clock.tick(self.FPS)