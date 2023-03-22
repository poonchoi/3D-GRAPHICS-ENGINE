import pygame as pg
import math as m
from MatrixMath import matrix as mm

class App:
    def __init__(self):
        pg.init()
        self.res = self.width, self.height = 1000, 700
        self.hwidth, self.hheight = self.width / 2, self.height / 2
        self.fps = 60
        self.screen = pg.display.set_mode(self.res)
        self.clock = pg.time.Clock()

        # vertices of cube
        self.points = [mm.Matrix([[100, 100, 100, 1]]),mm.Matrix([[100, -100, 100, 1]]),mm.Matrix([[-100, -100, 100, 1]]),mm.Matrix([[-100, 100, 100, 1]]),
                       mm.Matrix([[100, 100, 10, 1]]),mm.Matrix([[100, -100, 10, 1]]),mm.Matrix([[-100, -100, 10, 1]]),mm.Matrix([[-100, 100, 10, 1]])]
        #self.points = [mm.Matrix([[0, 100, 3, 1]])]
        self.fov = 45
        self.f = 1 / m.tan(m.radians(self.fov)/2)
        self.zf = 1000
        self.zn = .1
        self.g = self.zf / (self.zf - self.zn)
        self.a = self.height / self.width
        self.angle = m.radians(1)

        self.proj = mm.Matrix([[self.a*self.f, 0, 0, 0],
                               [0, self.a*self.f, 0, 0],
                               [0, 0, self.zf/(self.zf-self.zn), 1],
                               [0, 0, (-self.zf*self.zn) / (self.zf-self.zn), 0]])
        
        # self.proj = mm.Matrix([[self.a*self.f, 0, 0, 0],
        #                        [0, self.a*self.f, 0, 0],
        #                        [0, 0, self.g, 1],
        #                        [0, 0, -self.zn*self.g, 0]])


    def rotx(self, point):
        rotx = mm.Matrix([[1, 0, 0, 0],
                          [0, m.cos(self.angle), -m.sin(self.angle), 0],
                          [0, m.sin(self.angle), m.cos(self.angle), 0],
                          [0, 0, 0, 1]])
        return point * rotx
    
    def roty(self, point):
        roty = mm.Matrix([[m.cos(self.angle), 0, m.sin(self.angle), 0],
                          [0, 1, 0, 0],
                          [-m.sin(self.angle), 0, m.cos(self.angle), 0],
                          [0, 0, 0, 1]])
        return point * roty
    
    def rotz(self, point):
        rotz = mm.Matrix([[m.cos(self.angle), -m.sin(self.angle), 0, 0],
                          [m.sin(self.angle), m.cos(self.angle), 0, 0],
                          [0, 0, 1, 0],
                          [0, 0, 0, 1]])
        return point * rotz 
    

    def draw(self):
        self.screen.fill((255, 255, 255))

        for i in range(len(self.points)):
            self.points[i] = self.roty(self.points[i])
            #self.project(self.points[i])
            #self.project_ortho(self.points[i])
            
    
    def project_ortho(self, point):
        pg.draw.circle(self.screen, (0), (point[0][0] + self.hwidth, point[0][1] + self.hheight), 1)


    def project(self, point):
        projected = point * self.proj

        if projected[0][3] != 0:
            projected[0][0] /= projected[0][3]
            projected[0][1] /= projected[0][3]
            projected[0][2] /= projected[0][3]
            projected[0][3] /= projected[0][3]

            x, y = projected[0][0], projected[0][1]
            pg.draw.circle(self.screen, (0), (x + self.hwidth, y + self.hheight), 1)

            return (projected[0][0], projected[0][1], projected[0][2], projected[0][3])


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