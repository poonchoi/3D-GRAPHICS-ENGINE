import pygame as pg
from camera import *
from projection import *
from object3d import *

class App:
    def __init__(self):
        pg.init()
        self.res = self.width, self.height = 1600, 900
        self.h_width, self.h_height = self.width // 2, self.height // 2
        self.fps = 60
        self.screen = pg.display.set_mode(self.res)
        self.clock = pg.time.Clock()
        self.create_objects()

    def create_objects(self):
        self.camera = Camera(self, [0,0,0,1])
        self.projection = Projection(self)
        self.object = Object(self)

    def draw(self):
        self.screen.fill(pg.Color("black"))
        self.object.draw()

    def run(self):
        while True:
            self.draw()

            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            pg.display.set_caption(f"{round(self.clock.get_fps())} FPS")
            pg.display.flip()
            self.clock.tick(self.fps)

if __name__ == "__main__":
    app = App()
    app.run()