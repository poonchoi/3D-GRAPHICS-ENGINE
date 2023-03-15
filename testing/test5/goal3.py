import pygame as pg
import math as m
from MatrixMath import matrix as mm

class App:
    def __init__(self):
        pg.init()
        self.res = self.width, self.height = 500, 500
        self.hwidth, self.hheight = self.width / 2, self.height / 2
        self.fps = 60
        self.screen = pg.display.set_mode(self.res)
        self.clock = pg.time.Clock()

        # self.points = [mm.Matrix([[100, 100, 5, 1]]),mm.Matrix([[100, -100, 5, 1]]),mm.Matrix([[-100, -100, 5, 1]]),mm.Matrix([[-100, 100, 5, 1]]),
        #                mm.Matrix([[100, 100, 10, 1]]),mm.Matrix([[100, -100, 10, 1]]),mm.Matrix([[-100, -100, 10, 1]]),mm.Matrix([[-100, 100, 10, 1]])]
        self.points = [mm.Matrix([[100, 100, 1, 1]]),mm.Matrix([[100, -100, 1, 1]]),mm.Matrix([[-100, -100, 1, 1]]),mm.Matrix([[-100, 100, 1, 1]]),
                       mm.Matrix([[100, 100, 10, 1]]),mm.Matrix([[100, -100, 10, 1]]),mm.Matrix([[-100, -100, 10, 1]]),mm.Matrix([[-100, 100, 10, 1]])]

        self.fov = m.pi / 3
        self.f = 1 / m.tan(self.fov/2)
        self.zf = 1000
        self.zn = .1
        self.g = self.zf / (self.zf - self.zn)
        self.a = self.height / self.width

        self.proj = mm.Matrix([[self.a*self.f, 0, 0, 0],
                               [0, self.f, 0, 0],
                               [0, 0, self.zf/(self.zf-self.zn), 1],
                               [0, 0, (-self.zf*self.zn) / (self.zf-self.zn), 0]])


    def draw(self):
        self.screen.fill((255, 255, 255))
        for point in self.points:
            a = self.project(point)
            if a != None:
                x, y = a[0], a[1]
                pg.draw.circle(self.screen, (0), (x + self.hwidth, y + self.hheight), 4)
            #pg.draw.circle(self.screen, (0), (self.hwidth, self.hheight), 4)


    def rotate(self):
        pass


    def project(self, point):
        projected = point * self.proj

        if projected[0][3] != 0:
            projected[0][0] /= projected[0][3]
            projected[0][1] /= projected[0][3]

            return (projected[0][0], projected[0][1])
        else:
            return None


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