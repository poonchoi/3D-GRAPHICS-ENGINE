import pygame as pg
import MatrixMath.matrix as mm
from matrices import *

class App:
    def __init__(self):
        pg.init()
        self.res = self.width, self.height = 600, 600
        self.hwidth, self.hheight = self.height // 2, self.height // 2
        self.fps = 60
        self.screen = pg.display.set_mode(self.res)
        self.clock = pg.time.Clock()


    def draw(self):
        self.screen.fill((255, 255, 255))


    def run(self):
        while True:
            self.draw()

            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            pg.display.set_caption(f"{round(self.clock.get_fps())} FPS")
            pg.display.flip()
            self.clock.tick(self.fps)


class Camera():
    def __init__(self, res):
        self.pos = mm.Matrix([0, 0, 0, 1])
        self.forward = mm.Matrix([0, 0, 1, 1])
        self.up = mm.Matrix([0, 1, 0, 1])
        self.right = mm.Matrix([1, 0, 0, 1])
        self.hfov = 60
        self.a = res[1] / res[0]
        self.vfov = self.hfov * self.a
        self.near = 0.1
        self.far = 100
        self.speed = 1
        self.angle = [0, 0]
        self.aspeed = 0.1


    def movement(self):
        key = pg.key.get_pressed()

        if key[pg.K_w]:
            self.pos += self.forward * self.speed

        if key[pg.K_s]:
             self.pos -= self.forward * self.speed

        if key[pg.K_a]:
             self.pos -= self.right * self.speed

        if key[pg.K_d]:
             self.pos += self.right * self.speed

        if key[pg.K_RIGHT]:
            self.angle[1] += self.aspeed
            self.pitch()

        if key[pg.K_LEFT]:
            self.angle[1] -= self.aspeed
            self.pitch()

        if key[pg.K_UP]:
            self.angle[0] += self.aspeed
            self.yaw()

        if key[pg.K_DOWN]:
            self.angle[0] -= self.aspeed
            self.yaw()
    

    def yaw(self):
        self.forward *= rotate_y(self.angle[1])
        self.right *= rotate_y(self.angle[1])
        self.up *= rotate_y(self.angle[1])


    def pitch(self):
        self.forward *= rotate_x(self.angle[1])
        self.right *= rotate_x(self.angle[1])
        self.up *= rotate_x(self.angle[1])


if __name__ == "__main__":
    app = App()
    app.run()