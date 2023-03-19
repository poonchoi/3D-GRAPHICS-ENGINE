import pygame as pg
import math as m
import numpy as np

class App:
    def __init__(self):
        pg.init()
        self.res = self.width, self.height = 1000, 700
        self.hwidth, self.hheight = self.width / 2, self.height / 2
        self.fps = 60
        self.screen = pg.display.set_mode(self.res)
        self.clock = pg.time.Clock()

        self.fov = m.pi / 3
        self.f = 1 / m.tan(self.fov/2)
        self.zf = 1000
        self.zn = .1
        self.g = self.zf / (self.zf - self.zn)
        self.a = self.height / self.width
        self.angle = 0.01

        self.proj = np.array([
            [self.a*self.f, 0, 0, 0],
            [0, self.a*self.f, 0, 0],
            [0, 0, self.zf/(self.zf-self.zn), 1],
            [0, 0, (-self.zf*self.zn)/(self.zf-self.zn), 0]])
        
        self.points = [np.array([100, 100, 1, 1]),np.array([100, -100, 1, 1]),np.array([-100, -100, 1, 1]),np.array([-100, 100, 1, 1]),
                       np.array([100, 100, 3, 1]),np.array([100, -100, 3, 1]),np.array([-100, -100, 3, 1]),np.array([-100, 100, 3, 1])]

    def rotx(self):
        rotx = np.array([[1, 0, 0, 0],
                          [0, m.cos(self.angle), -m.sin(self.angle), 0],
                          [0, m.sin(self.angle), m.cos(self.angle), 0],
                          [0, 0, 0, 1]])
        return rotx
    
    def roty(self):
        roty = np.array([[m.cos(self.angle), 0, m.sin(self.angle), 0],
                          [0, 1, 0, 0],
                          [-m.sin(self.angle), 0, m.cos(self.angle), 0],
                          [0, 0, 0, 1]])
        return roty
    
    def rotz(self):
        rotz = np.array([[m.cos(self.angle), -m.sin(self.angle), 0, 0],
                          [m.sin(self.angle), m.cos(self.angle), 0, 0],
                          [0, 0, 1, 0],
                          [0, 0, 0, 1]])
        return rotz 
    
    
    def project(self, point):
        projected = point @ self.proj
        if projected[3] != 0:
            projected[0] /= projected[3]
            projected[1] /= projected[3]
            return (projected[0], projected[1])
        else:
            return None


    def draw(self):
        self.screen.fill((255, 255, 255))

        for i in range(len(self.points)):
            #self.points[i] = self.points[i] @ self.roty()
            self.points[i] = self.points[i] @ self.rotz()
            projected = self.project(self.points[i])
            if projected != None:
                x, y = projected[0], projected[1]
                pg.draw.circle(self.screen, (0), (x + self.hwidth, y + self.hheight), 1)


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